const TripSummary = ({ route }) => {
  if (!route) return null;

  return (
    <div>
      <h2>📊 Trip Summary</h2>

      <p><strong>Total Distance:</strong> {route.distance_km} km</p>
      <p><strong>Total Duration:</strong> {route.duration_hr} hrs</p>
    </div>
  );
};

export default TripSummary;