import React, { useEffect, useState } from 'react'
import { getagence, addagence, editagence , deleteagence} from '../services/APIService'
import AddAgence from './AddAgence'
import EditAgence from './EditAgence'

export default function PatientList() {

const [patients, setPatients] = useState([])
const [showAddPatientForm, setShowAddPatientForm] = useState(false)
const [showEditPatientForm, setShowEditPatientForm] = useState(false)
const [selectedEditData, setSelectedEditData] = useState()

useEffect(() => {
    
    let mount = true
    getagence()
    .then(res => {console.log("res from api", res)
        setPatients(res)
        return() => mount = false
    })
}, [])

const handleAddSubmit = (e) => {
    addagence(e.target)
    .then(res => {
        setPatients(res)
    })
}

const handleEditBtn = (agence) => {
    setSelectedEditData(agence)
    console.log("agence selected is", agence)
    setShowEditPatientForm(true)
    setShowAddPatientForm(false)
}

const handleEditSubmit = (e, id) => {
    editagence(id, e.target)
    .then(res => {
        setPatients(res)
    })
}
function handleCancelBtn() {
    setShowAddPatientForm(false)
}
const handleDeleteBtn = (id) => {
    deleteagence(id)
    .then(res => {
        setPatients(patients.filter(p=> p.patient_id !== id))
    })
}

  return (
    <>
    <h3>PATIENT LIST</h3>
    <table border={"2px"} cellPadding={"10px"}>
        <thead>
            <tr>
                <td>First Name</td>
                <td>Last Name</td>
                <td>Blood Group</td>
                <td>Action</td>
            </tr>
        </thead>
        <tbody>
            {patients.map(agence => {
                return <tr key={agence.patient_id}>
                <td>{agence.first_name}</td>
                <td>{agence.last_name}</td>
                <td>{agence.blood}</td>
                <td><button onClick={()=>handleEditBtn(agence)}>Edit</button> <button onClick={()=>handleDeleteBtn(patient.patient_id)}>Delete</button></td>
            </tr>
            })}
            
        </tbody>
    </table>
    <button onClick={()=>setShowAddPatientForm(true)}>Add New Patient</button>
    {showAddPatientForm && <AddAgence handleAddSubmit={handleAddSubmit} handleCancelBtn = {handleCancelBtn}/>}
    {showEditPatientForm && <EditAgence handleEditSubmit={handleEditSubmit} selectedEditData = {selectedEditData}/>}
    </>
  )
}
