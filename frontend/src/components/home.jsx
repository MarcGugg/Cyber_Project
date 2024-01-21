import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { NavLink } from "react-router-dom";
import { ReactSearchAutocomplete } from 'react-search-autocomplete'


export default function Home() {
    const [data, setData] = useState(null);
    const [companiesArray, setCompaniesArray] = useState(null)

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


    useEffect(() => {
        if (data) {
            //give each company a proper 'name' key bc ReactSearchAutocomplete expects every item
            //to have a name key. errors out otherwise.
            setCompaniesArray(data.map(company => ({ name: company.company, ...company })));
            console.log('companies array after assignment', companiesArray)
        }
    }, [data])

    useEffect(() => {
        console.log('companies array', companiesArray)
    }, [companiesArray])

    const handleOnSearch = (string, results) => {
        console.log(string, results);
    };

    const handleOnHover = (result) => {
        console.log(result);
    };

    const handleOnSelect = (item) => {
        console.log(item.name);
    };

    const handleOnFocus = () => {
        console.log("Focused");
    };

    const handleOnClear = () => {
        console.log("Cleared");
    };

    return (
        <>
            {data ?
                <div>
                    {companiesArray ?        
                      <div style={{ width: 200, margin: 20 }}>
                      <h2>Search for a company</h2>
                      {/* <div style={{ marginBottom: 20 }}>Try to type a company name</div> */}
                      <ReactSearchAutocomplete
                        items={companiesArray}
                        maxResults={5}
                        onSearch={handleOnSearch}
                        onHover={handleOnHover}
                        onSelect={handleOnSelect}
                        onFocus={handleOnFocus}
                        onClear={handleOnClear}
                        // fuseOptions={{ keys: ["name", "description"] }} // Search in the description text as well
                        fuseOptions={{ keys: ["name", "id"] }} // Search in the description text as well
                        styling={{ zIndex: 3 }} // To display it on top of the search box below
                      />
                    </div>
                    : <p>no search</p>}
                    {data.map(company => (
                        <NavLink key={company.id} to={`/companies/${company.id}`}>
                            <p key={company.id}>{company.company}</p>
                        </NavLink>
                    ))}
                </div> 
                : 
                <p>There are no companies</p>
            }
        </>
    );
}