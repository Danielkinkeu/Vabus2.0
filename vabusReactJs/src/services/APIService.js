import axios from "axios";

export  function getagence() {
  return axios.get('http://127.0.0.1:8000/api/gestionAgences/agenceList/')
  .then(res => {
    return res.data
  })}

export  function addagence(agence) {
return axios.post('http://127.0.0.1:8000/api/gestionAgences/add_agence/',
{
    agence_id: null,
    name: agence.name.value,
    picture: agence.picture.value,
    siege: agence.siege.value,
    telephone: agence.telephone.value,
    description: agence.description.value,
    published: agence.published.value,

})
.then(res => {
    return res.data
})}

export  function editagence(id, agence) {
    return axios.put('http://127.0.0.1:8000/api/gestionAgences/'+id+'/update_agence/',
    {
    name: agence.name.value,
    picture: agence.picture.value,
    siege: agence.siege.value,
    telephone: agence.telephone.value,
    description: agence.description.value,
    published: agence.published.value,
    })
    .then(res => {
        return res.data
    })}

export  function deleteagence(id) {
    return axios.delete('http://127.0.0.1:8000/api/gestionAgences/'+id+'/delete_agence/')
    .then(res => {
        return res.data
    })}
