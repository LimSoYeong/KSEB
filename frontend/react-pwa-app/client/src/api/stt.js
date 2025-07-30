import axios from 'axios';

const BASE_URL = import.meta.env.VITE_MODEL_SERVER_URL;

export async function requestSTT(audioFile) {
  const formData = new FormData();
  formData.append('file', audioFile);

  const response = await axios.post(`${BASE_URL}/stt`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

  return response.data.text;
}