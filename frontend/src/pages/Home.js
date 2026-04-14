import React, { useState } from "react";
import TripForm from "../components/TripForm";
import MapView from "../components/MapView";
import TripPlan from "../components/TripPlan";
import LogViewer from "../components/LogViewer";
import TripSummary from "../components/TripSummary";
import { planTrip } from "../services/api";

const Home = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (form) => {
    try {
      setLoading(true);
      setError("");
      setData(null);

      const res = await planTrip(form);

      console.log("[DEBUG] API Response:", res.data);

      if (res.data.error) {
        setError(res.data.error);
      } else {
        setData(res.data);
      }
    } catch (err) {
      console.error("[ERROR]", err);
      setError("Backend connection failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1 className="title">🚛 Truck Trip Planner</h1>

      {/* 🔥 TOP SECTION (FORM + MAP) */}
      <div className="top-section">
        {/* LEFT: FORM */}
        <div className="form-card">
          <TripForm onSubmit={handleSubmit} />
        </div>

        {/* RIGHT: MAP */}
        <div className="map-card">
          <MapView path={data?.route?.path} />
        </div>
      </div>

      {/* 🔹 Loading */}
      {loading && <p className="center">⏳ Generating trip plan...</p>}

      {/* 🔹 Error */}
      {error && <p className="error">❌ {error}</p>}

      {/* 🔥 BOTTOM SECTION */}
      {data && (
        <>
          {/* Summary */}
          <div className="card">
            <TripSummary route={data.route} />
          </div>

          {/* Plan */}
          <div className="card">
            <TripPlan plan={data.plan} />
          </div>

          {/* Logs */}
          <div className="card">
            <LogViewer logs={data.logs} />
          </div>
        </>
      )}
    </div>
  );
};

export default Home;