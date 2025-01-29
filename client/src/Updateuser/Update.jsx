import "./Update.css";
import { useState, useEffect } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import { toast } from "react-hot-toast";

export default function Update() {
    const initialUser = {
        name: "",
        email: "",
        address: "",
    };

    const [user, setUser] = useState(initialUser);
    const navigate = useNavigate();
    const { id } = useParams();

    const Formhandler = (e) => {
        const { name, value } = e.target;
        setUser((prevUser) => ({ ...prevUser, [name]: value }));
    };

    useEffect(() => {
        axios.get(`http://localhost:8000/api/user/${id}`)
            .then((response) => {
                setUser(response.data);
            })
            .catch((error) => {
                console.log(error);
                toast.error("Failed to fetch user data", { position: "top-right" });
            });
    }, [id]);

    

    const Submitform = async (e) => {    
        e.preventDefault();
        try {
            const response = await axios.put(`http://localhost:8000/api/update/user/${id}`, user)
            console.log("User updated successfully");
            toast.success(response.data.message, { position: "top-right" });
            navigate('/');
        } catch (error) {
            console.error("Error updating user:", error);
            toast.error("Failed to update user", { position: "top-right" });
        }
    };

    return (
        <>
            <div className="main-wrapper">
                <div className="home-page-link"> 
                    <Link to="/">Back <i className="fa-solid fa-backward"></i></Link>
                </div>
                <div className="Updateuser-form">
                    <form className="main-container" onSubmit={Submitform}>
                        <h3>Update User</h3>
                        <div className="form-group user-form">
                            <label htmlFor="name" className="label-control">Name:</label>
                            <input type="text" className="form-control" name="name" autoComplete="off" placeholder="Enter your name" onChange={Formhandler} value={user.name} />
                        </div>
                        <div className="form-group user-form">
                            <label htmlFor="email" className="label-control">Email:</label>
                            <input type="email" className="form-control" name="email" autoComplete="off" placeholder="Enter your email" onChange={Formhandler} value={user.email} />
                        </div>
                        <div className="form-group user-form">
                            <label htmlFor="address" className="label-control">Address:</label>
                            <input type="text" className="form-control" name="address" autoComplete="off" placeholder="Enter your address" onChange={Formhandler} value={user.address} />
                        </div>
                        <div className="form-group">
                            <button className="btn btn-update" type="submit">Update</button>
                        </div>
                    </form>
                </div>
            </div>
        </>
    );
}
