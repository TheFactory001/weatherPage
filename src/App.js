import { useState } from 'react';
import './App.css';
import WeatherDisplay from './Components/WeatherDisplay';

function App() {

  const [city, setCity] = useState();
  const [temperature, setTemperature] = useState(0);

  const handleClickWeatherButton = async (e) => {
    e.preventDefault();
    const city = e.target.elements.city.value.trim();
    setCity(city)
    const rawResponse = await fetch('http://127.0.0.1:5000/getWeatherInfo', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ city })
    });
    const content = await rawResponse.json();
    setTemperature(content.temperature)
  }


  return (
    <div className="App">
      <form onSubmit={handleClickWeatherButton}>
        <input type="text" placeholder="City" name="city" required/>
        <button>Get Weather Info</button> 
      </form>
      <div>
        <WeatherDisplay city={city} temperature={temperature} />
      </div>
    </div>
  );
}

export default App;
