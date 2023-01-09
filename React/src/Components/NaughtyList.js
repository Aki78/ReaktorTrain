import React, { useState, useEffect } from 'react';
import "./NaughtyList.css"

function List({list}) {

  const [filteredList, setFilteredList] = useState([]);

  useEffect(() => {
    // I did not look into the data, but is the idea that you only show one entry per pilot_id?
    // Because I think this only shows only the closest drone from each pilot. Also there is no real ordering to the list? Is this intentional?
    const minValues = list.reduce((acc, curr) => {
      // If acc[curr.pilot_id] == 0, !acc[curr.pilot_id] == true and the current value will replace it..? 
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

