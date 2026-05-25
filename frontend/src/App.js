import axios from 'axios'
import {useEffect,useState} from 'react'

function App(){

const [records,setRecords]=useState([])
const [file,setFile]=useState(null)

useEffect(()=>{
loadRecords()
},[])

function loadRecords(){

axios.get(
'http://127.0.0.1:8000/api/records/'
)

.then(response=>{

setRecords(response.data)

})

}

function uploadFile(){

const formData=new FormData()

formData.append(
'file',
file
)

axios.post(
'http://127.0.0.1:8000/api/upload/',
formData
)

.then(()=>{

alert('Upload Success')

loadRecords()

})

}

return(

<div style={{padding:'20px'}}>

<h1>ESG Dashboard</h1>

<input
type="file"
onChange={(e)=>setFile(e.target.files[0])}
/>

<button onClick={uploadFile}>
Upload CSV
</button>

<br/><br/>

<table border="1">

<thead>

<tr>
<th>ID</th>
<th>Source</th>
<th>Category</th>
<th>Quantity</th>
<th>Status</th>
</tr>

</thead>

<tbody>

{
records.map(record=>(

<tr key={record.id}>

<td>{record.id}</td>
<td>{record.source}</td>
<td>{record.category}</td>
<td>{record.quantity}</td>
<td>{record.status}</td>

</tr>

))
}

</tbody>

</table>

</div>

)

}

export default App