import React, { useState, useEffect } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import axios from 'axios';

export default function oneCompany() {

    const {companyId} = useParams() //companyId will be used to fetch company from the backend

    return (
        <></>
    )
}