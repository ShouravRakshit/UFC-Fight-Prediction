import { useState } from 'react';
import axios from 'axios';
import { TextField, Button } from '@mui/material';

const PredictForm = () => {
    const [inputData, setInputData] = useState('');
    const [prediction, setPrediction] = useState('');
    const [message, setMessage] = useState('');

    const handlePredict = async () => {
        try {
            const response = await axios.post('http://localhost:8000/api/todos/predict/', {
                input_data: inputData,
            });
            if (response.status === 200) {
                setPrediction(response.data.prediction);
                setMessage('Prediction successful!');
            } else {
                setMessage('Prediction failed.');
            }
        } catch (error) {
            console.error('Error making prediction:', error);
            setMessage('Error making prediction.');
        }
    };

    return (
        <div>
            <TextField
                label="Input Data (comma-separated)"
                value={inputData}
                onChange={(e) => setInputData(e.target.value)}
                fullWidth
            />
            <Button
                variant="contained"
                color="primary"
                onClick={handlePredict}
                style={{ marginTop: '10px' }}
            >
                Predict
            </Button>
            {message && <p>{message}</p>}
            {prediction && <p>Prediction: {prediction}</p>}
        </div>
    );
};

export default PredictForm;
