import "./App.css"
import User from "./getUser/User.jsx"
import Adduser from "./Adduser/Adduser.jsx"
import Update from "./Updateuser/Update.jsx"
import Delete from "./Deleteuser/Delete.jsx"
import {RouterProvider, createBrowserRouter} from "react-router-dom"

export default function App() {

  const route = createBrowserRouter([
    {
    path:'/',
    element:<User/>,
    },
    {
      path:"/add",
      element:<Adduser/>,
    }, 
    {
      path:"update/:id",
      element:<Update/>
    },
    {
      path:"delete/:id",
      element:<Delete/>
    }
  ]);
    return (
      <>
        <h1>MERN STACK</h1>
        <div className="wrapper">
          <div className="form-group">
              <RouterProvider router={route}></RouterProvider>
            </div>
          
          </div>
        
      </>
    )
}

