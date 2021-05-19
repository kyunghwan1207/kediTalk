import React, { useEffect, useState } from 'react';
import {Link} from 'react-router-dom';
import '../../css/Navi.css';

function Navi(){
    let pgN = document.location.href.split('/')[3]
    let [underline, setUnderline] = useState({left:"0%"})

    useEffect(()=>{
        pgN === "like"
        ? setUnderline({left:"50%"})
        : setUnderline({left:"0%"})
    },[pgN])
    

    return(
        <>
        <div className="navi-container">
            <div className="navi-box">
                <Link className="navi-" to="/">
                    <span role = "img" aria-label = "하트">⏰피드</span>
                </Link>
                <Link className="navi-" to="/like">
                    <span role = "img" aria-label = "질문">🤞추천</span>
                </Link>
                {/* ko */}

                <Link className="navi-" to="/visit">
                    <span role = "img" aria-label = "질문">🤞방문</span>
                </Link>
                <Link className="navi-" to="/reserve">
                    <span role = "img" aria-label = "질문">🤞예약</span>
                </Link>
                <Link className="navi-" to="/review">
                    <span role = "img" aria-label = "질문">🤞리뷰</span>
                </Link>
                <Link className="navi-" to="/scrap">
                    <span role = "img" aria-label = "질문">🤞스크랩</span>
                </Link>
                <div className="navi-underline" style={underline}></div>
            </div>
        </div>
        </>
    )
}
export default Navi;