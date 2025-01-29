import "./User.css";
import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import uploadIcon from "../assets/images/upload.png";  // Update icon
import deleteIcon from "../assets/images/delete.png";  // Delete icon
import toast from "react-hot-toast";

export default function User() {
    const [Users, SetUsers] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get("http://localhost:8000/api/users");
                SetUsers(response.data);
            } catch (error) {
                console.log("Error while getting data", error);
            }
        };
        fetchData();
    }, []);

    const deleteUser = async (userId) => {
        try {
            const response = await axios.delete(`http://localhost:8000/api/delete/user/${userId}`);
            
            SetUsers((prevUsers) => prevUsers.filter((user) => user._id !== userId));
    
            toast.success(response.data.message, { position: "top-right" });
        } catch (error) {
            console.error("Error deleting user:", error);
            toast.error("Failed to delete user", { position: "top-right" });
        }
    };
    
    return (
        <>
            <div className="UserTable">
                <Link to="/add" className="Link Link-primary">
                    Add-User <img src={uploadIcon} alt="Add User" className="icon" />
                </Link>

                {Users.length === 0 ? (
                    <div className="noData">
                        <h3>No data to display</h3>
                        <p>Please add a new user.</p>
                    </div>
                ) : (
                    <table className="table table-bordered">
                        <thead>
                            <tr>
                                <th>S.No</th>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Address</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {Users.map((user, index) => (
                                <tr key={user._id}>
                                    <td>{index + 1}</td>
                                    <td>{user.name}</td>
                                    <td>{user.email}</td>
                                    <td>{user.address}</td>
                                    <td className="actionLink-container">
                                        <Link to={`/update/${user._id}`} className="Link Link-action Link-success">
                                            <img src={uploadIcon} alt="Edit" className="icon" />
                                        </Link>
                                        <Link className="Link Link-action Link-danger" onClick={() => deleteUser(user._id)}>
                                            <img src={deleteIcon} alt="Delete" className="icon" />
                                        </Link>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </>
    );
}
