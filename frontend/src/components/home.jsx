import React from 'react'
import { useEffect, useState } from 'react'
import axios from 'axios'

// http://127.0.0.1:8000
export default function Home() {
    const [data, setData] = useState(null)
    let res = ''
    useEffect(() => {
        
        async function fetchData() {
            res = await axios("http://127.0.0.1:8000/companies", {
                method: 'GET',
                // headers: {'Content-Type':'Access-Control-Allow-Origin'}
            })
        }
        
        fetchData()

    }, [data])

    if (res) {
        setData(res)
    }

    return (
        <>
        {data ? 
        <p>These are the companies</p>
        : 
        <p>There are no companies</p>
        }
        </>
    )
}