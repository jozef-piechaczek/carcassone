import React, {Component} from 'react';
import './error.css'

class Error extends Component {

    componentDidUpdate(prevProps, prevState, snapshot) {
        if (this.props?.message || this.props?.data) {
            console.warn('An error happened\n' +
                'Message:', this.props?.message, '\n',
                'Data:', this.props?.data)
        }
    }

    render() {
        return (
            <div
                style={{height: this.props?.message && "45px"}}
                className="m-error-popup"
            >
                <p className="m-error-popup-p">{this.props?.message}</p>
            </div>
        );
    }
}

export default Error;