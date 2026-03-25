import axios from "axios";

const API = "http://localhost:8000";

export const getScore = (data) => axios.post(`${API}/score/`, data);
export const extractGoals = (text) => axios.post(`${API}/goals/`, { text });