import { useEffect, useState } from 'react'

export default function App() {
  const [status, setStatus] = useState('loading...')
  useEffect(() => {
    fetch('/api/health')
      .then(r => r.json())
      .then(d => setStatus(d.status ?? JSON.stringify(d)))
      .catch(e => setStatus('error: ' + e))
  }, [])
  return (
    <div style={{ fontFamily: 'system-ui', padding: 24 }}>
      <h1>Wishlist (dev)</h1>
      <p>API health: {status}</p>
    </div>
  )
}
