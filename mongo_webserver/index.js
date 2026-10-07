import express from "express"
import mongoose  from "mongoose"
import bodyParser from "body-parser"
import dotenv from "dotenv"
import route from "./routes/userRoutes.js"
import cors from "cors"



const app = express();

app.use(cors());

app.use(bodyParser.json());

dotenv.config();

const PORT = process.env.PORT || 7000;
const MONGOURL = process.env.MONGO_URL;

console.log("Mongo URL:", process.env.MONGO_URL);

const message = "connected";

// Fix: Correct the syntax of the `app.get` route
app.get('/', (req, res) => {  // Arrow function syntax
    res.json({
        message
    });
});

mongoose
        .connect(MONGOURL)
        .then(() => {
            console.log("DB CONNECT SUCCESSFULLY");
            app.listen(PORT, () => {
                console.log(`Server is active at : http://localhost:${PORT}`);
            });
        })
        .catch((error) => console.log(error));

app.use("/api", route);
