import './App.css';
import Points from './Components/Points'
import NaughtyList from './Components/NaughtyList'

function App() {
  return (
    <div className="App">
	  <h2> Zone Entered </h2>
	  <Points/>
	  <h1>list of contact information</h1>
	  <NaughtyList/>
    </div>
  );
}

export default App;
