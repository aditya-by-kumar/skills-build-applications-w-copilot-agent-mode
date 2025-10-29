const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : '/api/activities/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Activities endpoint:', endpoint);
        console.log('Fetched activities:', results);
      });
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h1 className="mb-4 text-primary">Activities</h1>
      <div className="card shadow-sm">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-primary">
              <tr>
                <th>#</th>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Date</th>
                <th>User</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((a, i) => (
                <tr key={a.id || i}>
                  <td>{i + 1}</td>
                  <td>{a.type}</td>
                  <td>{a.duration}</td>
                  <td>{a.date}</td>
                  <td>{a.user?.name || a.user}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
import React, { useEffect, useState } from 'react';
