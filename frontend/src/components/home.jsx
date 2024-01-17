import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function Home() {
    const [data, setData] = useState(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await axios.get("http://127.0.0.1:8000/companies");
                setData(response.data);
            } catch (error) {
                console.error("Error fetching data:", error);
                // Handle error if needed
            }
        }

        fetchData();
    }, []); // Pass an empty dependency array to run the effect only once when the component mounts

    return (
        <>
            {data ?
                <div>
                    <p>These are the companies</p>
                    {data.map(company => {
                        <div>{company.name}</div>
                    })}
                </div> 
                : 
                <p>There are no companies</p>
            }
        </>
    );
}