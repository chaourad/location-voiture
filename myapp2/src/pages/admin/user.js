import { Link } from 'react-router-dom';
import './nav.css';
import './table.css';

import { useEffect, useState } from 'react';

function Users() {
    useEffect(() => {
      let sidebar = document.querySelector(".sidebar");
      let closeBtn = document.querySelector("#btn");
  
      closeBtn.addEventListener("click", ()=>{
        sidebar.classList.toggle("open");
        menuBtnChange();
      });
  
   
  
      function menuBtnChange() {
        if(sidebar.classList.contains("open")){
          closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
        }else {
          closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
        }
      }
    }, []); 

    const [user , setusers]=useState([])
  
    useEffect(() => {
      fetch('http://127.0.0.1:8000/client')
        .then((response) => response.json())
        .then((data) => setusers(data))
        .catch((error) => console.error('Error:', error));
    }, []);

    return (
      <div>
        <meta charSet="UTF-8" />
        <link rel="stylesheet" href="style.css" />
        <link href="https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <div className="sidebar">
          <div className="logo-details">
         
            <div className="logo_name">Admin</div>
            <i className="bx bx-menu" id="btn" />
          </div>
          <ul className="nav-list">
            
            <li>
              <a href="/cars">
                <i className="bx bx-grid-alt" />
                <span className="links_name">Dashboard</span>
              </a>
              <span className="tooltip">Dashboard</span>
            </li>
            <li>
              <a href="/users">
                <i className="bx bx-user" />
                <span className="links_name">User</span>
              </a>
              <span className="tooltip">User</span>
            </li>
            <li>

         
        <Link  to="/reservation" >
                <i className="bx bx-chat" />
                <span className="links_name">Reservation</span>
                </Link>
              <span className="tooltip">Reservation</span>
            </li>
           
        
        <li className="profile">
          <div className="profile-details">
            <div className="name_job">
              <div className="name">Logout</div>
            </div>
          </div>
          <Link  to="/login" >
          <i className="bx bx-log-out" id="log_out" style={{cursor : "pointer"}} />
        </Link>
        </li>
      </ul>
    </div>
    <section class="home-section">
   
    <section className="ftco-section">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-md-6 text-center mb-5">
              <h2 className="heading-section">Users</h2>
            </div>
          </div>
          <div className="row">
            <div className="col-md-12">
              <div className="table-wrap">
                <table className="table">
                  <thead className="thead-dark">
                    <tr>
                      <th>ID </th>
                      <th>Username</th>
                      <th>age</th>
                      <th>date_permis</th>
                      <th>ref_permis</th>
                      <th>Email</th>
                      <th>password</th>
                    </tr>
                  </thead>
                  <tbody>
                  {user.map((user, index) => (
                    <tr className="alert" role="alert" key={index}>
                      <td>{user.id}</td>
                      <th scope="row">{user.username}</th>
                      <td>{user.age}</td>
                      <td>{user.date_permis}</td>
                      <td>{user.ref_permis}</td>
                      <td>{user.email}</td>
                      <td>{user.password}</td>
                    </tr>
                    ))} 
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </section>
      </section>
  </div>
    );

}
  
export default Users;