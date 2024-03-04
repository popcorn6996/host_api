from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test-internet-speed', methods=['GET'])
def test_internet_speed():
    import speedtest
    
    st = speedtest.Speedtest()
    
    print('Testing Internet Speed')
    
    download_speed = st.download() / 10 **6
    upload_speed = st.upload() / 10 **6
    ping_speed = st.results.ping
    
    result = {
        'download_speed': f'{download_speed:.2f} Mbps',
        'upload_speed': f'{upload_speed:.2f} Mbps',
        'ping_speed': f'{ping_speed:.2f} ms'
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
