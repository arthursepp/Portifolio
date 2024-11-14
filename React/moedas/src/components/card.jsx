import React, { useState, useEffect } from 'react';
import './style/card.css';

const Card = () => {
  const [currencies, setCurrencies] = useState([]);
  const [baseCurrency, setBaseCurrency] = useState('');
  const [targetCurrency, setTargetCurrency] = useState('');
  const [exchangeRate, setExchangeRate] = useState(null);

  useEffect(() => {
    fetch('https://economia.awesomeapi.com.br/json/available/uniq')
      .then(response => response.json())
      .then(data => {
        setCurrencies(Object.keys(data));
      })
      .catch(error => console.error('Erro ao buscar dados da API:', error));
  }, []);

  useEffect(() => {
    if (baseCurrency && targetCurrency) {
      fetch(`https://economia.awesomeapi.com.br/json/last/${baseCurrency}-${targetCurrency}`)
        .then(response => response.json())
        .then(data => {
          const rateKey = `${baseCurrency}${targetCurrency}`;
          setExchangeRate(data[rateKey]);
        })
        .catch(error => console.error('Erro ao buscar dados da API:', error));
    }
  }, [baseCurrency, targetCurrency]);

  return (
    <div className='card'>
      <select
        name="baseCurrency"
        id="baseCurrency"
        onChange={(e) => setBaseCurrency(e.target.value)}
        value={baseCurrency}
      >
        <option value="" disabled>Selecione a moeda base</option>
        {currencies.map(currency => (
          <option value={currency} key={currency}>
            {currency}
          </option>
        ))}
      </select>
      <select
        name="targetCurrency"
        id="targetCurrency"
        onChange={(e) => setTargetCurrency(e.target.value)}
        value={targetCurrency}
      >
        <option value="" disabled>Selecione a moeda alvo</option>
        {currencies.map(currency => (
          <option value={currency} key={currency}>
            {currency}
          </option>
        ))}
      </select>
      {exchangeRate && (
        <div>
          <p>1 {baseCurrency} = {exchangeRate.bid} {targetCurrency}</p>
        </div>
      )}
    </div>
  );
};

export default Card;