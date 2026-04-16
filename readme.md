# Static Routing using SDN Controller (Ryu + Mininet)

## 📌 Project Title

Static Routing using SDN Controller

---

## 📖 Description

This project demonstrates static routing using Software Defined Networking (SDN) with the Ryu controller and Mininet emulator.

The controller installs flow rules manually to define routing paths between hosts. Packet forwarding decisions are controlled centrally using SDN principles.

---

## 🎯 Objectives

* Implement static routing using SDN controller
* Install flow rules manually
* Validate packet delivery using Mininet
* Ensure routing path consistency (regression test)

---

## 🛠️ Technologies Used

* Python
* Ryu SDN Controller
* Mininet
* OpenFlow Protocol

---

## 📂 Project Files

* `controller.py` → Ryu controller logic
* `topology.py` → Custom Mininet topology (optional)
* `README.md` → Documentation

---

## ▶️ How to Run

### Step 1: Activate environment

```bash
 source ~/ryu-env/bin/activate
```

### Step 2: Run Ryu Controller

```bash
python3 -m ryu.cmd.manager ryu.app.simple_switch_13
```

### Step 3: Run Mininet (in another terminal)

```bash
sudo mn --topo linear,3 --controller=remote --switch ovsk --mac
```

### Step 4: Test connectivity

```bash
mininet> pingall
```

---

## ✅ Expected Output

* Successful connection between hosts
* `0% packet loss`
* Flow rules installed in switch

---

## 🔍 Observations

* Controller receives packet-in events
* Flow rules are dynamically installed
* Network traffic follows defined paths

---

## 🔁 Regression Test

Re-running the controller maintains consistent routing behavior.

---

## 📌 Conclusion

Static routing was successfully implemented using an SDN controller. The centralized control allowed efficient traffic management and predictable routing paths.

---

## 👨‍💻 Author

Amith B A
