import React, { useState } from 'react'

function Child(props) {

    const[msg,setMsg]=useState("Good night")


    function sendtoParent(){

        props.sendTo(msg);
    }
  return (
    <div>Child
        <pre>
            {
                JSON.stringify(msg)
            }
        </pre>

        <button className='btn btn-danger' onClick={sendtoParent}>Send  Data</button>


    </div>
  )
}

export default Child