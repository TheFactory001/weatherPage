import React from 'react';

function WeatherDisplay(props) {
    return (
      <div className="WeatherComp">
        <h3>{props.city}</h3>
        <p>{props.temperature} degrees celsius</p>
      </div>
    );
  }

  export default WeatherDisplay;