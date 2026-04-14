import axios from "axios";

const API = axios.create({
  baseURL: "https://trip-planner-app-ewa2.onrender.com/api"
});

export const planTrip = (data) => API.post("plan-trip/", data);