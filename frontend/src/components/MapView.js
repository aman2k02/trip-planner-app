import { MapContainer, TileLayer, Polyline, Marker, Popup } from "react-leaflet";
import { useEffect, useRef } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet/dist/leaflet.css";


// 🔥 FIX marker icon issue
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});


const MapView = ({ path }) => {
  const mapRef = useRef();

  // 🔥 Auto fit map to route
  useEffect(() => {
    if (path && path.length > 0 && mapRef.current) {
      const bounds = path.map((p) => [p[0], p[1]]);
      mapRef.current.fitBounds(bounds, {
        padding: [50, 50],
        maxZoom: 12,
      });
    }
  }, [path]);

  return (
    <div>
      <h2 style={{ marginBottom: "10px" }}>🗺️ Route Map</h2>

      <div style={{ height: "350px", width: "100%" }}>
        <MapContainer
          center={[28.6, 77.2]}
          zoom={5}
          style={{ height: "100%", width: "100%", borderRadius: "10px" }}
          whenCreated={(mapInstance) => {
            mapRef.current = mapInstance;
          }}
        >
          <TileLayer
            attribution="&copy; OpenStreetMap contributors"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />

          {/* 🔹 Route */}
          {path && path.length > 0 && (
            <>
              <Polyline positions={path} color="blue" weight={4} />

              {/* 🔥 START MARKER */}
              <Marker position={path[0]}>
                <Popup>🚩 Start</Popup>
              </Marker>

              {/* 🔥 END MARKER */}
              <Marker position={path[path.length - 1]}>
                <Popup>🏁 End</Popup>
              </Marker>
            </>
          )}
        </MapContainer>
      </div>
    </div>
  );
};

export default MapView;