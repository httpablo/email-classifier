import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

export const analyzeEmail = async (formData: FormData) => {
  const response = await api.post("/analyze", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return response.data;
};
