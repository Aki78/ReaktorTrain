import React, { useState, useEffect } from 'react';
import "./NaughtyList.css"

function List({list}) {

  const [filteredList, setFilteredList] = useState([]);

  useEffect(() => {
    // Here, the list filtered only for the closest distance
    // The list is not ordered
    const minValues = list.reduce((acc, curr) => {
      if (!acc[curr.pilot_id] || acc[curr.pilot_id].distance > curr.distance) {
        acc[curr.pilot_id] = curr;
      }
      return acc;
    }, {});

    let new_list = Object.values(minValues);
    setFilteredList(new_list)

  }, [list]);

  return (
    <table>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Phone Number</th>
          <th>Email</th>
          <th>Closest Distance</th>
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

