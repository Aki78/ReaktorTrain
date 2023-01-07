import React, { useState, useEffect } from 'react';

function List() {
  const [list, setList] = useState([]);
  const [filteredList, setFilteredList] = useState([]);

  async function fetchList() {
    try {
      const response = await fetch('http://localhost:12345/fetch_recent_naughty_pilots');
      const data = await response.json();
      setList(data);
      // console.log(data)
    } catch (error) {
      console.error(error);
    }
  }

  // Call the function every 1.9 seconds
  useEffect(() => {
    const interval = setInterval(fetchList, 1900);
	  // get unique pilots with the closest distance
	const minValues = list.reduce((acc, curr) => {
	  if (!acc[curr.pilot_id] || acc[curr.pilot_id].distance > curr.distance) {
	    acc[curr.pilot_id] = curr;
	  }
  return acc;
}, {});

    const new_list = Object.values(minValues);
	  setFilteredList(new_list)
    console.log("filtededList: ", filteredList)
    return () => clearInterval(interval);

  }, []);


  return (
    <div>
	{filteredList.map(item => (
	  <div key={item.id}>
	    {item.firstName} {item.lastName}: {item.phoneNumber} ({item.email}) : {item.distance} meters
	  </div>
	))}
    </div>
  );
}

export default List;

