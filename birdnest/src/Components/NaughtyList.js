import React, { useState, useEffect } from 'react';

function List() {
  const [list, setList] = useState([]);

  async function fetchList() {
    try {
      const response = await fetch('http://localhost:12345/fetch_recent_naughty_pilots');
      const data = await response.json();
      setList(data);
      console.log(data)
    } catch (error) {
      console.error(error);
    }
  }

  // Call the function every 1.9 seconds
  useEffect(() => {
    const interval = setInterval(fetchList, 1900);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
	{list.map(item => (
	  <div key={item.id}>
	    {item.firstName} {item.lastName}: {item.phoneNumber} ({item.email})
	  </div>
	))}

    </div>
  );
}

export default List;

