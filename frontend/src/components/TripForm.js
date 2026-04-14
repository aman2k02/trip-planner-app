import React, { useState } from "react";
import axios from "axios";

const TripForm = ({ onSubmit }) => {
  const [form, setForm] = useState({
    current_location: "",
    pickup_location: "",
    dropoff_location: "",
    cycle_used: 0,
  });

  const [suggestions, setSuggestions] = useState([]);
  const [activeField, setActiveField] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSearch = async (value, field) => {
    setActiveField(field);

    if (!value) {
      setSuggestions([]);
      return;
    }

    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/api/search-location/?q=${value}`
      );
      setSuggestions(res.data);
    } catch (err) {
      console.error("Search error:", err);
    }
  };

  const handleSelect = (value) => {
    setForm({ ...form, [activeField]: value });
    setSuggestions([]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form);
  };

  return (
    <div>
      <h2>📍 Enter Trip Details</h2>

      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column" }}>
        
        {/* Current */}
        <input
          name="current_location"
          placeholder="Current Location"
          value={form.current_location}
          onChange={(e) => {
            handleChange(e);
            handleSearch(e.target.value, "current_location");
          }}
          style={{ marginBottom: "10px" }}
        />

        {/* Pickup */}
        <input
          name="pickup_location"
          placeholder="Pickup Location"
          value={form.pickup_location}
          onChange={(e) => {
            handleChange(e);
            handleSearch(e.target.value, "pickup_location");
          }}
          style={{ marginBottom: "10px" }}
        />

        {/* Drop */}
        <input
          name="dropoff_location"
          placeholder="Dropoff Location"
          value={form.dropoff_location}
          onChange={(e) => {
            handleChange(e);
            handleSearch(e.target.value, "dropoff_location");
          }}
          style={{ marginBottom: "10px" }}
        />

        {/* Suggestions */}
        {suggestions.length > 0 && (
          <div
            style={{
              border: "1px solid #ccc",
              borderRadius: "5px",
              marginBottom: "10px",
              background: "white"
            }}
          >
            {suggestions.map((s, i) => (
              <div
                key={i}
                style={{
                  padding: "8px",
                  cursor: "pointer",
                  borderBottom: "1px solid #eee"
                }}
                onClick={() => handleSelect(s.name)}
              >
                📍 {s.name}
              </div>
            ))}
          </div>
        )}

        {/* Cycle */}
        <input
          name="cycle_used"
          type="number"
          placeholder="Cycle Used (hrs)"
          value={form.cycle_used}
          onChange={handleChange}
          style={{ marginBottom: "10px" }}
        />

        <button
          type="submit"
          style={{ marginTop: "10px" }}
          disabled={
            !form.current_location ||
            !form.pickup_location ||
            !form.dropoff_location
          }
        >
          🚀 Plan Trip
        </button>
      </form>
    </div>
  );
};

export default TripForm;