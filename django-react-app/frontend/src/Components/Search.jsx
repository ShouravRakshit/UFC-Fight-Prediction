import { useState } from 'react';
import axios from 'axios';
import { TextField, Button, CircularProgress } from '@mui/material';

const Search = () => {
    const [query, setQuery] = useState('');
    const [description, setDescription] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSearch = async () => {
        setLoading(true);
        setDescription('');  // Clear previous description
        try {
            console.log(`Searching for: ${query}`);
            const response = await axios.get(`http://localhost:8000/api/todos/search/?q=${query}`);
            console.log('Response:', response.data);
            if (response.data.length > 0) {
                console.log(response.data[0].description)
                setDescription(response.data[0].description);
            } else {
                setDescription('No results found');
            }
        } catch (error) {
            console.error('Error searching for title:', error);
            setDescription('Error searching for title');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <TextField
                label="Search Title"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyPress={(e) => {
                    if (e.key === 'Enter') {
                        handleSearch();
                    }
                }}
            />
            <Button
                variant="contained"
                color="primary"
                onClick={handleSearch}
                style={{ marginLeft: '10px' }}
            >
                Search
            </Button>
            {loading && <CircularProgress style={{ marginLeft: '10px' }} />}
            {description && <p>{description}</p>}
        </div>
    );
};

export default Search;
