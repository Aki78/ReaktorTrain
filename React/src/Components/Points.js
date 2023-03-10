import "./Points.css"
import getColor from "./utils.js"

function Points({list}) {


  return (
    <div className="container">
      {list.map(point => (
        <div
          key={point.X}
          className="point"
          style={{
            left: point.X/1000 - 500/4,
            top: point.Y/1000 - 500/4,
	    backgroundColor: getColor(point.pilot_id)
          }}
	                data-tooltip={point.firstName + " " + point.lastName}
          onMouseOver={e => e.currentTarget.classList.add('pointHover')}
          onMouseOut={e => e.currentTarget.classList.remove('pointHover')}
        />
      ))}
    </div>
  );
}

export default Points;

