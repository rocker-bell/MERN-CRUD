import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import "./Adduser.css";
import { toast } from "react-hot-toast";

export default function Adduser() {
    const initialUser = {
        name: "",
        email: "",
        address: "",
    };

    const [user, setUser] = useState(initialUser);
    const navigate = useNavigate();

    const Formhandler = (e) => {
        const { name, value } = e.target;
        setUser((prevUser) => ({ ...prevUser, [name]: value }));
    };

    const Submitform = async (e) => {    
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/user', user);
            console.log("User created successfully");
            toast.success(response.data.message, { position: "top-right" });
            navigate('/');
        } catch (error) {
            console.error("Error creating user:", error);
            toast.error("Failed to create user", { position: "top-right" });
        }
    };

    return (
        <>
            <div className="main-wrapper">
                <div className="home-page-link"> 
                    <Link to="/">Back <i className="fa-solid fa-backward"></i></Link>
                </div>
                <div className="Adduser-page">
                    <form className="main-container" onSubmit={Submitform}>
                        <h3>Add User</h3>
                        <div className="form-group user-form">
                            <label htmlFor="name" className="label-control">Name:</label>
                            <input type="text" className="form-control" name="name" autoComplete="off" placeholder="Enter your name" onChange={Formhandler} />
                        </div>
                        <div className="form-group user-form">
                            <label htmlFor="email" className="label-control">Email:</label>
                            <input type="email" className="form-control" name="email" autoComplete="off" placeholder="Enter your email" onChange={Formhandler} />
                        </div>
                        <div className="form-group user-form">
                            <label htmlFor="address" className="label-control">Address:</label>
                            <input type="text" className="form-control" name="address" autoComplete="off" placeholder="Enter your address" onChange={Formhandler} />
                        </div>
                        <div className="form-group">
                            <button className="btn btn-submit btn-primary" type="submit">Submit</button>
                        </div>
                    </form>
                </div>
            </div>
        </>
    );
}
