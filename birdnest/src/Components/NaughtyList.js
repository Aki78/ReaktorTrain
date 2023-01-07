import React, { useState, useEffect } from 'react';
import "./NaughtyList.css"

function List() {
  let count = 0
  const [list, setList] = useState([]);
  const [filteredList, setFilteredList] = useState([]);

  async function fetchList() {
    try {
      const response = await fetch('http://localhost:12345/fetch_recent_naughty_pilots');
      const data = await response.json();
      setList(data);
      console.log("data: ", data)
    } catch (error) {
      console.error(error);
    }



  }


  useEffect(() => {
    const minValues = list.reduce((acc, curr) => {
      if (!acc[curr.pilot_id] || acc[curr.pilot_id].distance > curr.distance) {
        acc[curr.pilot_id] = curr;
      }
      return acc;
    }, {});

    let new_list = Object.values(minValues);
    console.log("new_list: ", new_list)
    setFilteredList(new_list)
    console.log("filtededList: ", filteredList)
    console.log(count+=1)

  }, [list]);

  // Call the function every 1.9 seconds
  useEffect(() => {
    const interval = setInterval(fetchList, 1900);
    return () => clearInterval(interval);

  }, []);


  return (
    <table>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Phone Number</th>
          <th>Email</th>
          <th>Distance</th>
        </tr>
      </thead>
      <tbody>
        {filteredList.map(item => (
          <tr key={item.email} >
            <td>{item.firstName}</td>
            <td>{item.lastName}</td>
            <td>{item.phoneNumber}</td>
            <td>{item.email}</td>
            <td>{item.distance} meters</td>
          </tr>
        ))}
      </tbody>
    </table>
  );

}

export default List;

