import logo from './logo.svg';
import './App.css';

function App() {
  function handleClick(e) {
    console.log(e)
    e.preventDefault();
    fetch("/snippets/125/")
    .then((response) => response.json())
    .then((json) => {
        console.log(json)
        alert(JSON.stringify(json))
    });
  }

  return (
    <div>
      <h1>Demo React App</h1>
      <button onClick={handleClick}>Click me</button>
    </div>
  );
}

export default App;
