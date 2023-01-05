import logo from './logo.svg';
import './App.css';
import Points from './Components/Points'
import NaughtyList from './Components/NaughtyList'

const points = [
  { id: 1, x: 50, y: 50 },
  { id: 2, x: 100, y: 100 },
  { id: 3, x: 150, y: 150 },
];

function App() {
  return (
    <div className="App">
      <header className="App-header">
	  <Points points={points} />
	  <NaughtyList/>
      </header>
    </div>
  );
}

export default App;
