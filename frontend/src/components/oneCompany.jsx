import React, { useState, useEffect } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import axios from 'axios';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Tab } from '@mui/material';

export default function OneCompany() {

    const {companyId} = useParams() //companyId will be used to fetch company from the backend

    const [company, setCompany] = useState(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/companies/${companyId}`);
                setCompany(response.data);
                console.log(response.data)
            } catch (error) {
                console.error("Error fetching data:", error);
                // Handle error if needed
            }
        }

        fetchData()
    }, []); // Pass an empty dependency array to run the effect only once when the component mounts

    useState(() => {
        console.log('company', company)
    }, [company])

    return (
        <>
        {company ? 
        <div>

        <h2>{company.company}</h2>
        <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Year Founded</h3></TableCell>
                <TableCell>{company.yearFounded}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}> 
                <TableCell><h3>Category</h3></TableCell>
                <TableCell>{company.category.category}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}> 
                <TableCell><h3>Subcategory</h3></TableCell>
                <TableCell>{company.subcategory}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Company URL</h3></TableCell>
                <TableCell>{company.companyUrl}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>LinkedIn URL</h3></TableCell>
                <TableCell>{company.linkedinUrl}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Corporate Customers</h3></TableCell>   
                <TableCell>{company.corporateCustomers}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Customer Count</h3></TableCell>
                <TableCell>{company.customerCount}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Customer Industries</h3></TableCell>
                <TableCell>{company.customerIndustries}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Customer Size</h3></TableCell>
                <TableCell>{company.customerSize}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Employee Count</h3></TableCell>
                <TableCell>{company.employees}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Headcount Direction</h3></TableCell>
                <TableCell>{company.headcountDirection}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Executive Team</h3></TableCell>
                <TableCell>{company.executiveTeam}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>HQ Location</h3></TableCell>
                <TableCell>{company.hqCity}, {company.hqCountry}</TableCell>
                {/* HQ city and country most likely won't match bc the seed data is */}
                {/* randomly generated. this shouldn't be a problem when using real data */}
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Industry Awards</h3></TableCell>
                <TableCell>{company.industryAwards}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Industry Events</h3></TableCell>
                <TableCell>{company.industryEvents}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Pricing</h3></TableCell>
                <TableCell>{company.pricing}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Product Integrations</h3></TableCell>
                <TableCell>{company.productIntegrations}</TableCell>
            </TableRow>
            <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                <TableCell><h3>Tech Stack</h3></TableCell>
                <TableCell>{company.techStack}</TableCell>
            </TableRow>

          </TableHead>
        </Table>
      </TableContainer>
      {company.fundingDetails.length ?
        <div>
            {company.fundingDetails.map((detail, index) => (
                <div>
                    <h2>{`Funding Details ${index + 1}`}</h2>
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Amount Raised</h3></TableCell>
                                    <TableCell>{detail.amountRaised}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Category</h3></TableCell>
                                    <TableCell>{detail.category}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>CEO</h3></TableCell>
                                    <TableCell>{detail.ceo}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Date Of Funding</h3></TableCell>
                                    <TableCell>{detail.dateOfFunding}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Employee Count</h3></TableCell>
                                    <TableCell>{detail.employees}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Established</h3></TableCell>
                                    <TableCell>{detail.established}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Funding Round</h3></TableCell>
                                    <TableCell>{detail.fundingRound}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Lead Investor</h3></TableCell>
                                    <TableCell>{detail.leadInvestor}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Location</h3></TableCell>
                                    <TableCell>{detail.location}</TableCell>
                                </TableRow>
                                <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell><h3>Total Amount Raised</h3></TableCell>
                                    <TableCell>{detail.totalAmountRaised}</TableCell>
                                </TableRow>
                            </TableHead>
                        </Table>
                    </TableContainer>
                </div>
            ))}
        </div> 
      : ''}
        </div>
        : 
        <p>No Company</p>}
        </>
    )
}