import { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Checkbox, FormControlLabel } from '@mui/material';

const AddTodo = () => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [completed, setCompleted] = useState(false);
    const [message, setMessage] = useState('');

    const handleAddTodo = async () => {
        try {
            const response = await axios.post('http://localhost:8000/api/todos/add_todo/', {
                title,
                description,
                completed
            });
            if (response.status === 201) {
                setMessage('Todo added successfully!');
            } else {
                setMessage('Failed to add todo.');
            }
        } catch (error) {
            console.error('Error adding todo:', error);
            setMessage('Error adding todo.');
        }
    };

    return (
        <div>
            <TextField
                label="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                fullWidth
            />
            <TextField
                label="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                fullWidth
                multiline
                rows={4}
                style={{ marginTop: '10px' }}
            />
            <FormControlLabel
                control={
                    <Checkbox
                        checked={completed}
                        onChange={(e) => setCompleted(e.target.checked)}
                        color="primary"
                    />
                }
                label="Completed"
                style={{ marginTop: '10px' }}
            />
            <Button
                variant="contained"
                color="primary"
                onClick={handleAddTodo}
                style={{ marginTop: '10px' }}
            >
                Add Todo
            </Button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default AddTodo;
