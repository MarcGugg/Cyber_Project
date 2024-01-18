import React, { useState, useEffect } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import axios from 'axios';

export default function OneCompany() {

    const {companyId} = useParams() //companyId will be used to fetch company from the backend

    const [data, setData] = useState(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/companies/${companyId}`);
                setData(response.data);
            } catch (error) {
                console.error("Error fetching data:", error);
                // Handle error if needed
            }
        }

        fetchData();
    }, []); // Pass an empty dependency array to run the effect only once when the component mounts

    useState(() => {
        console.log('company', data)
    }, [data])

    return (
        <>
        {data ? 
        <p>One Company</p>
        : 
        <p>No Company</p>}
        </>
    )
}