from flask import Flask,request,redirect,render_template,url_for
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def username():
    if request.method == 'POST':
        user = request.form['username']
        return redirect (url_for('topic', username= user))
    return render_template ('index.html')

@app.route('/topic')
def topic():
    username = request.args.get('username')
    topics =['Kinematics','Newtons laws of motion','Work power and energy',
             'Rotation','Gravitation',"Centre of Mass and Collisions",'Thermodynamics',"Mechanical Properties of Fluids","Mechanical Properties of Solids",
             'SHM',"Waves","Kinetic Theory","Electricity","Magnetism","Optics","Nuclei","Atoms","Communication","Semiconductors",
             "Dual Nature","EM Waves"]
    return render_template('topics.html', username=username, topics=topics)


@app.route("/concept/<topic_name>")
def concept(topic_name):
    username = request.args.get('username')
    content = conceptsdict.get(topic_name, "No content available.")
    return render_template("concept.html",title=topic_name,topic=topic_name,topic_name=topic_name,content=content,username=username)

@app.route('/quiz/<topic_name>',methods = ["GET","POST"])
def quiz(topic_name):
    qns = quizqns[topic_name]
    username = request.args.get('username')
    if request.method == "POST":
        mo = 0
        i = 0
        for q in qns:
            user_ans = request.form.get(f"q{i}")
            if user_ans==q['answer']:
                mo += 1
            i +=1

        total= len(qns)
        percentage = (mo/total)*100
        if percentage==100:
            feedback = 'Excellent job ! You mastered the concepts 👑'
        elif percentage >= 80:
            feedback = 'Good Job ! keep doing well'
        elif percentage >= 50:
            feedback= "Nice work! Read the concepts again for better results.Don't loose hope." 
        else:
            feedback= 'Give some time to understand concepts clearly and practise again !'
        return render_template('result.html',score = mo , total=len(qns),topic_name=topic_name,feedback=feedback,username=username)

    return render_template('quiz.html',topic_name=topic_name,quizqns = qns,username=username)



conceptsdict={"Kinematics": """
KINEMATICS

INTRODUCTION
Kinematics is the branch of mechanics that deals with the description of motion without
considering the cause of motion. It focuses on how objects move—covering concepts like
distance, displacement, speed, velocity, and acceleration. Motion can occur in a straight line
(rectilinear motion), along a curve, or in any general path in space.

TYPES OF MOTION
1) ONE–DIMENSIONAL (1D) MOTION
   Motion along a straight line.
   Examples: A car moving on a straight road, a ball dropped from a height.

2) TWO–DIMENSIONAL (2D) MOTION
   Motion in a plane.
   Examples: Projectile motion, circular motion.

3) THREE–DIMENSIONAL (3D) MOTION
   Motion in space.
   Examples: Motion of an airplane, movement of planets.

BASIC QUANTITIES OF MOTION
1) DISTANCE
   • Total length of the path travelled.
   • Scalar quantity.
   • Always positive.
   Example: If you walk 10 m east and 10 m west, distance = 20 m.

2) DISPLACEMENT
   • Shortest distance between initial and final positions.
   • Vector quantity.
   • Can be positive, negative, or zero.
   Example: In the same walk above, displacement = 0.

3) SPEED
   • Rate of change of distance.
   • Scalar quantity.
   • Formula: speed = distance / time.
   • Types:
     – Uniform speed: constant speed.
     – Variable speed: changes with time.
     – Average speed: total distance / total time.
     – Instantaneous speed: speed at a particular instant.

4) VELOCITY
   • Rate of change of displacement.
   • Vector quantity.
   • Formula: velocity = displacement / time.
   • Types:
     – Uniform velocity
     – Variable velocity
     – Average velocity
     – Instantaneous velocity
   • Velocity has both magnitude and direction.

ACCELERATION
Acceleration is the rate of change of velocity with respect to time.
Formula: a = (v – u) / t
Where:
u = initial velocity  
v = final velocity  
t = time  
a = acceleration  

• Acceleration can be positive or negative.
• Negative acceleration is called retardation or deceleration.

EQUATIONS OF UNIFORMLY ACCELERATED MOTION
Valid only when acceleration is constant.

1) v = u + at  
2) s = ut + (1/2)at²  
3) v² = u² + 2as  
4) s = ((u + v)/2) t  

Where:
s = displacement  
t = time taken  

These equations are extremely useful in solving numerical problems.

GRAPHICAL REPRESENTATION OF MOTION
Graphs help visualize motion and understand changes in displacement, velocity, and acceleration.

1) DISTANCE–TIME GRAPH
   • Slope gives speed.

2) VELOCITY–TIME GRAPH
   • Slope gives acceleration.
   • Area under graph gives displacement.

3) ACCELERATION–TIME GRAPH
   • Area under graph gives change in velocity.

UNIFORM MOTION
Motion with constant velocity.
Displacement vs time graph is a straight line.

NON–UNIFORM MOTION
Motion with changing velocity.
Graph becomes curved.

RELATIVE VELOCITY
Relative velocity of object A with respect to B:
V_AB = V_A – V_B

Examples:
• Two cars moving in same direction → relative velocity decreases.
• Two cars moving in opposite directions → relative velocity increases.

FREE FALL
When objects fall freely under gravity alone.
Acceleration = g = 9.8 m/s² (approx 10 m/s²)

Equations of motion become:
v = u + gt  
h = ut + (1/2)gt²  
v² = u² + 2gh  

PROJECTILE MOTION BASICS (IMPORTANT)
Though part of 2D motion, some points overlap with kinematics:

• Horizontal velocity remains constant.  
• Vertical motion is under gravity.  
• Path of projectile is parabolic.  

TERMS USED IN PROJECTILE MOTION
• Time of flight  
• Maximum height  
• Range  

These depend on initial velocity and angle of projection.

DIFFERENCE BETWEEN SCALAR & VECTOR QUANTITIES
SCALAR → has magnitude only (speed, distance, mass).  
VECTOR → has magnitude + direction (velocity, displacement, acceleration).

AVERAGE VS INSTANTANEOUS VALUES
Average speed = total distance / total time  
Instantaneous speed = speed at a particular moment  

AN IMPORTANT POINT
Velocity can be zero even when speed is not zero.
Example: A body moving in a circular track returns to starting point → displacement = 0, so velocity = 0, but speed ≠ 0.

COMMON MISTAKES TO AVOID
• Confusing distance with displacement.
• Using equations of motion when acceleration is not constant.
• Ignoring direction in vector quantities.
• Treating average speed same as average velocity (they are different).

APPLICATIONS OF KINEMATICS
• Vehicle motion analysis  
• Sports science  
• Space missions (trajectory planning)  
• Robotics  
• Projectile prediction (missiles, balls in sports)

SUMMARY
• Kinematics describes motion without explaining causes.
• Basic concepts: distance, displacement, speed, velocity, acceleration.
• Equations of motion apply only for constant acceleration.
• Graphs provide deep insights into motion.
• Relative velocity helps analyze motion between objects.
• Free fall and projectile motion are special cases of accelerated motion.

Kinematics forms the foundation of mechanics and is essential for solving complex problems
in physics, engineering, space science, and technology.

""", "Newtons laws of motion": """
NEWTON'S LAWS OF MOTION

INTRODUCTION
Newton’s Laws of Motion form the foundation of classical mechanics. These laws describe the
relationship between the forces acting on a body and its motion. They apply to all objects
moving at normal everyday speeds (much slower than the speed of light). Together, the three
laws provide a complete framework to understand how objects begin to move, continue to move,
or stop moving.

FORCE
Before understanding the laws, it is important to know what force is.
• Force is a push or pull acting on a body.
• It can change the state of motion of a body or its shape.
• Force is a vector quantity, meaning it has both magnitude and direction.
• SI unit of force: Newton (N).

NEWTON'S FIRST LAW OF MOTION (LAW OF INERTIA)
Statement:
A body remains at rest or continues to move with uniform velocity unless acted upon by an
external unbalanced force.

This means:
• If no net force acts, a body will not change its motion.
• A resting object stays at rest.
• A moving object continues in a straight line with constant speed.

INERTIA
Inertia is the tendency of a body to resist changes in its state of rest or motion.
Three types:
1) Inertia of rest – body resists being moved.
2) Inertia of motion – body resists stopping.
3) Inertia of direction – body resists change in direction.

Examples:
• Dust falls off a carpet when shaken.
• Passengers fall forward when a moving bus stops suddenly.
• A body continues sliding on ice due to very low friction.

NEWTON'S SECOND LAW OF MOTION
Statement:
The rate of change of momentum of a body is directly proportional to the applied force and
takes place in the direction of the force.

Mathematically:
F = m × a

Where:
F = force  
m = mass  
a = acceleration  

Momentum (p) = m × v

Important points:
• Force is needed to change velocity (speed or direction).
• Greater the mass, greater the force needed for the same acceleration.
• If force is zero → acceleration is zero → uniform motion.

Examples:
• Kicking a football: harder kick → greater acceleration.
• Heavy objects require more force to move than lighter ones.

IMPULSE
Impulse = Force × Time
Impulse = Change in momentum

Examples:
• Batsman hitting a cricket ball.
• Airbags in cars increase time of impact → reduce force.

NEWTON'S THIRD LAW OF MOTION
Statement:
For every action, there is an equal and opposite reaction.

Meaning:
• Forces always occur in pairs.
• Action and reaction forces act on different bodies.

Examples:
• A gun recoils when a bullet is fired.
• A rocket moves upward because it pushes gases downward.
• Walking: we push the ground backward, ground pushes us forward.

IMPORTANT APPLICATIONS OF NEWTON’S LAWS
1) Walking, running, cycling, swimming.
2) Rocket propulsion.
3) Working of jet engines.
4) Recoil of guns.
5) Motion of vehicles.
6) Movement of planets (with gravity as force).
7) Safety devices like airbags and helmets.

FREE-BODY DIAGRAMS (FBD)
FBD is a simple diagram showing all forces acting on a body.
Common forces:
• Weight (mg)
• Normal reaction (N)
• Applied force (F)
• Friction (f)
• Tension (T)
• Air resistance

FRICTION
Friction is a force that opposes relative motion.

Types:
1) Static friction – prevents motion.
2) Kinetic friction – acts during motion.
3) Rolling friction – least among all.

Advantages of friction:
• Walking, writing, gripping objects.

Disadvantages:
• Wears out machines.
• Produces unwanted heat.

LAWS OF FRICTION
• Friction ∝ Normal force.
• Friction is independent of area of contact.
• Static friction > Kinetic friction.

MASS VS WEIGHT
Mass:
• Quantity of matter.
• Constant.
• SI unit: kg.

Weight:
• Force of gravity acting on a body.
• Changes with location.
• W = mg
• SI unit: N.

EQUILIBRIUM OF FORCES
A body is in equilibrium when:
• Net force = 0
• Net torque = 0

Examples:
• A book resting on a table.
• An object hanging motionless on a string.

MOMENTUM CONSERVATION
If no external force acts on a system, total momentum remains constant.

Examples:
• Recoil of a gun.
• Rocket propulsion.
• Collisions (elastic and inelastic).

SUMMARY
• First law defines inertia and states that no motion change occurs without force.
• Second law gives quantitative relation between force, mass, and acceleration.
• Third law explains the mutual interaction of bodies through action-reaction.
• Momentum, impulse, friction, FBDs, and equilibrium are essential extensions of NLM.
• These laws apply to almost all real-life motions and form the backbone of classical mechanics.

Understanding Newton’s Laws of Motion is crucial before moving to advanced topics like
work-energy theorem, momentum conservation, circular motion, and rotational mechanics.
""",'Work power and energy' :"""

1. WORK
• Work is said to be done when a force produces displacement in the direction of the force.
• Work (W) = Force × Displacement × cosθ
  - θ = angle between force and displacement.
• If θ = 0°, W = Fd  (maximum positive work)
• If θ = 90°, W = 0  (no work done; e.g., carrying a load)
• If θ = 180°, W = –Fd (negative work; force opposite to displacement)

2. KINETIC ENERGY (KE)
• Kinetic energy is the energy possessed by a body due to its motion.
• KE = ½mv²
• Work–Energy Theorem: Net work done = Change in kinetic energy.

3. POTENTIAL ENERGY (PE)
• Potential energy is the energy possessed by a body due to its position or configuration.
• Gravitational potential energy:
    PE = mgh
• Elastic potential energy (spring):
    PE = ½kx²

4. MECHANICAL ENERGY
• Mechanical energy = KE + PE
• In absence of non-conservative forces (like friction), total mechanical energy remains constant.

5. POWER
• Power is the rate of doing work.
• Power (P) = Work / Time
• Instantaneous power:
    P = F·v (dot product of force and velocity)
• SI unit = watt (W)

6. LAW OF CONSERVATION OF ENERGY
• Energy cannot be created or destroyed; it only transforms from one form to another.
• Total energy of an isolated system remains constant.

7. CONSERVATIVE AND NON-CONSERVATIVE FORCES
• Conservative forces (gravity, spring):
    - Work done is path-independent
    - Total mechanical energy conserved
• Non-conservative forces (friction):
    - Work done depends on path
    - Mechanical energy decreases

8. COLLISIONS (BASIC)
• Elastic collision – KE conserved.
• Inelastic collision – KE not conserved; momentum always conserved.
• Completely inelastic collision – bodies stick together.

""",'Rotation':"""Rotational motion refers to the motion of a body around a fixed axis. The key quantities in rotational motion are angular displacement, angular velocity, and angular acceleration.

1. Angular Displacement (θ): 
   - The angle through which a point or line has been rotated.
   - SI unit: radian (rad)

2. Angular Velocity (ω):
   - Rate of change of angular displacement.
   - ω = dθ/dt
   - SI unit: rad/s

3. Angular Acceleration (α):
   - Rate of change of angular velocity.
   - α = dω/dt
   - SI unit: rad/s²

4. Relation between linear and angular quantities:
   - v = rω
   - aₜ = rα  (tangential acceleration)
   - aᵣ = v²/r = rω²  (radial acceleration)

5. Moment of Inertia (I):
   - Measure of resistance to rotation.
   - Depends on mass distribution.
   - Common formulas:
     • I = MR² (ring)
     • I = (1/2)MR² (solid disc)
     • I = (2/5)MR² (solid sphere)

6. Torque (τ):
   - Rotational analogue of force.
   - τ = r × F = rF sinθ
   - SI unit: Newton-metre (N·m)

7. Rotational Kinetic Energy:
   - K = (1/2) Iω²

8. Angular Momentum (L):
   - L = Iω
   - Conserved in the absence of external torque.

9. Rolling Motion:
   - Combination of rotation + translation.
   - No-slip condition: v = Rω

10. Conservation Laws:
    - Mechanical energy conserved if no non-conservative forces.
    - Angular momentum conserved if net external torque = 0.
""",'Gravitation':"""**GRAVITATION**

Gravitation is the force of attraction between any two masses in the universe. Every object with mass attracts every other object with mass, no matter how small the force.

Newton's Law of Universal Gravitation states that the force between two bodies of masses m1 and m2 separated by distance r is:

        F = G * (m1 * m2) / r²

where  
G = universal gravitational constant = 6.67 × 10⁻¹¹ N m²/kg².

**Key Points:**
• Gravitational force is always attractive.  
• It acts along the line joining the centres of the two bodies.  
• It decreases as distance increases (inversely proportional to r²).  
• It increases with larger masses.  
• Gravity near Earth gives objects an acceleration of g = 9.8 m/s².  
• g decreases with height and increases with Earth's density.  

**Kepler’s Laws of Planetary Motion:**
1. The orbit of a planet is an ellipse with the Sun at one focus.  
2. A line joining a planet and the Sun sweeps equal areas in equal time intervals.  
3. The square of the time period of a planet is proportional to the cube of the semi-major axis of its orbit (T² ∝ R³).

Gravitational Potential Energy (U):
        U = -GMm / r  
Negative sign shows gravitational force is attractive.

Escape Velocity:
Minimum velocity needed to escape Earth's gravitational pull:
        ve = √(2gR) = 11.2 km/s for Earth.

Acceleration due to gravity on Earth:
        g = GM/R²  
Changes with height, depth, and latitude.
""","Centre of Mass and Collisions": """Centre of Mass (COM) is the point where the entire mass of a system can be considered to be concentrated for the purpose of analyzing motion. For a system of particles, the COM moves as if all external forces act only on it. The COM of a rigid body depends on mass distribution.

The position of COM for two particles is given by:
R = (m1*r1 + m2*r2) / (m1 + m2)

If no external force acts on a system, its centre of mass moves with constant velocity.

Collisions: A collision is an event where two bodies exert forces on each other for a short duration. During a collision, momentum is always conserved if no external force acts.

Types of Collisions:
1. Elastic Collision – Both momentum and kinetic energy are conserved.
2. Inelastic Collision – Momentum is conserved, but kinetic energy is not. Often bodies stick together (perfectly inelastic collision).

In one-dimensional elastic collisions, the final velocities are given by:
v1 = (m1 - m2)/(m1 + m2) * u1 + (2*m2)/(m1 + m2) * u2
v2 = (2*m1)/(m1 + m2) * u1 + (m2 - m1)/(m1 + m2) * u2

Coefficient of restitution (e):
e = (relative speed after collision) / (relative speed before collision)

For perfectly elastic collision: e = 1
For perfectly inelastic collision: e = 0

Momentum of the system before collision = Momentum after collision (if no external force).""",

'Thermodynamics' : """
THERMODYNAMICS

INTRODUCTION
Thermodynamics is the branch of physics that deals with heat, temperature, work, and the
energy transformations between them. It helps us understand engines, refrigerators, and
energy flow in physical systems.

BASIC TERMINOLOGY
1) SYSTEM
   A part of the universe chosen for study.
   Types:
   • Open system – exchanges mass and energy.
   • Closed system – exchanges only energy.
   • Isolated system – exchanges neither mass nor energy.

2) SURROUNDINGS
   Everything outside the system.

3) STATE VARIABLES
   Quantities that describe the state of a system:
   • Pressure (P)
   • Volume (V)
   • Temperature (T)
   • Internal energy (U)

4) PROCESS VARIABLES
   • Work (W)
   • Heat (Q)

TYPES OF THERMODYNAMIC PROCESSES
1) ISOTHERMAL PROCESS
   Temperature remains constant (T = constant).
   Boyle’s law applies: PV = constant.

2) ADIABATIC PROCESS
   No heat exchange (Q = 0).
   Follows: PV^γ = constant.

3) ISOCHORIC PROCESS
   Volume remains constant (V = constant).
   No work done (W = 0).

4) ISOBARIC PROCESS
   Pressure remains constant (P = constant).

INTERNAL ENERGY (U)
It is the total energy contained within a system (kinetic + potential energy of molecules).

FIRST LAW OF THERMODYNAMICS
∆Q = ∆U + W  
This expresses the conservation of energy.

• ∆Q → heat supplied  
• ∆U → change in internal energy  
• W → work done by system  

SIGN CONVENTION
• Heat added → +Q  
• Heat removed → –Q  
• Work done by system → +W  
• Work done on system → –W  

SECOND LAW OF THERMODYNAMICS
Heat cannot spontaneously flow from a colder body to a hotter body.
Entropy of the universe always increases.

HEAT ENGINE
A device that converts heat into work.
Efficiency: η = (Work output / Heat input)

REFRIGERATOR
Opposite of a heat engine.
Coefficient of performance (COP):  
COP = (Heat extracted from cold reservoir / Work done)

SPECIFIC HEAT CAPACITY (c)
Amount of heat required to raise the temperature of 1 kg of a substance by 1°C.

GAS LAWS
1) Boyle’s Law – P ∝ 1/V  
2) Charles’ Law – V ∝ T  
3) Gay–Lussac’s Law – P ∝ T  

IDEAL GAS EQUATION
PV = nRT  
Where:
• P = pressure  
• V = volume  
• n = number of moles  
• R = universal gas constant  
• T = temperature (Kelvin)  

ENTROPY
A measure of disorder/randomness in a system.
In irreversible processes, entropy increases.

APPLICATIONS
• Heat engines (cars, turbines)  
• Refrigerators and ACs  
• Power plants  
• Chemical reactions  
• Weather science  

SUMMARY
Thermodynamics deals with heat, work, energy, and the laws governing their transformation.
The first and second laws help understand machines, engines, refrigerators, and natural
processes involving heat.
""","Mechanical Properties of Solids": """
MECHANICAL PROPERTIES OF SOLIDS

1. WHAT IS A SOLID?
A solid has definite shape and volume. Its atoms are tightly packed and resist deformation.

2. STRESS
Stress = Force / Area
Types of stress:
• Tensile stress – stretching
• Compressive stress – squeezing
• Shearing stress – sliding layers

3. STRAIN
Strain = Change in length / Original length
(Strain has no units)

4. HOOKE’S LAW
Within elastic limit:
Stress ∝ Strain

5. ELASTIC MODULI
• Young’s Modulus (Y) = tensile stress / tensile strain
• Shear Modulus (η) = shearing stress / shearing strain
• Bulk Modulus (K) = -ΔP / (ΔV/V)

6. ELASTIC AND PLASTIC BEHAVIOUR
• Elastic – returns to original shape
• Plastic – permanent deformation

7. STRESS–STRAIN CURVE
Important points:
• Proportional limit
• Elastic limit
• Yield point
• Fracture point
""","Mechanical Properties of Fluids": """
MECHANICAL PROPERTIES OF FLUIDS

1. WHAT IS A FLUID?
A fluid flows when a force is applied. Includes liquids and gases.

2. PRESSURE IN FLUIDS
P = F / A
Unit: Pascal (Pa)

3. PASCAL’S LAW
Pressure applied to an enclosed fluid is transmitted equally in all directions.

4. HYDROSTATIC PRESSURE
P = hρg
Pressure increases with depth.

5. BUOYANCY (ARCHIMEDES’ PRINCIPLE)
Upthrust = weight of displaced fluid.

6. BERNOULLI’S PRINCIPLE
P + 1/2 ρv² + ρgh = constant

7. VISCOSITY
Resistance to flow.
Stoke’s Law: F = 6π η r v

8. SURFACE TENSION
Liquids behave like a stretched membrane.

9. CONTINUITY EQUATION
A₁v₁ = A₂v₁
Velocity increases when area decreases.
""","SHM": """
SIMPLE HARMONIC MOTION (SHM)

1. INTRODUCTION
Simple Harmonic Motion is a type of periodic motion in which a body oscillates to and fro
about a mean position under a restoring force proportional to displacement.

2. CHARACTERISTICS OF SHM
• Motion is periodic.
• Restoring force is proportional and opposite to displacement.
• Displacement, velocity, and acceleration vary sinusoidally.

3. RESTORING FORCE
F = –kx
Where:
k = force constant
x = displacement

4. ACCELERATION IN SHM
a = –ω² x
Where:
ω = angular frequency

5. DISPLACEMENT EQUATION
x(t) = A sin(ωt + φ)
A = amplitude
φ = phase constant

6. VELOCITY IN SHM
v = ω √(A² – x²)

7. ACCELERATION IN SHM
a = –ω² x
Maximum at extreme positions.

8. TIME PERIOD AND FREQUENCY
Time period:
T = 2π √(m/k)

Frequency:
f = 1/T

Angular frequency:
ω = 2πf = √(k/m)

9. ENERGY IN SHM
Total Energy (E) = 1/2 k A² (constant)
Kinetic Energy and Potential Energy continuously interchange.

10. EXAMPLES OF SHM
• Pendulum (small oscillations)
• Spring-mass system
• Vibrating tuning fork
• Oscillations of molecules
""","Waves": """
WAVES – CLASS 11 PHYSICS

1. INTRODUCTION
A wave is a disturbance that travels through a medium or space, carrying energy without actual transfer of matter.

2. TYPES OF WAVES
• Mechanical waves – require a medium (sound waves).
• Electromagnetic waves – do NOT require a medium (light).
• Transverse waves – particles vibrate perpendicular to propagation.
• Longitudinal waves – particles vibrate parallel to propagation.

3. CHARACTERISTICS OF WAVES
• Wavelength (λ): distance between two crests/troughs.
• Frequency (f): number of oscillations per second.
• Time period (T): time for one oscillation (T = 1/f).
• Amplitude (A): maximum displacement.
• Wave speed (v): speed of wave through a medium.

4. WAVE EQUATION
v = f λ
Where:
v = velocity, f = frequency, λ = wavelength

5. DISPLACEMENT EQUATION OF A WAVE
y(x, t) = A sin(kx – ωt)

6. SPEED OF SOUND
In solids > liquids > gases

In gases:
v = √(γRT / M)

7. PRINCIPLE OF SUPERPOSITION
When two waves overlap, the resultant displacement is the algebraic sum of individual displacements.

8. INTERFERENCE
Constructive interference:
A = A1 + A2

Destructive interference:
A = |A1 – A2|

9. STANDING WAVES
Formed due to superposition of two waves travelling in opposite directions with same frequency.

10. RESONANCE
Large amplitude oscillations produced when frequency of external force equals natural frequency.
""","Kinetic Theory": """

1. INTRODUCTION
The kinetic theory explains the macroscopic properties of gases in terms of the motion of molecules.

2. ASSUMPTIONS OF IDEAL GAS
• Gas is made of identical molecules.
• Molecules are point masses.
• No intermolecular forces except during collisions.
• Collisions are perfectly elastic.
• Average kinetic energy ∝ temperature.

3. PRESSURE OF A GAS
Pressure is created by continuous molecular collisions with container walls.

4. RMS SPEED
v_rms = √(3RT / M)

5. MEAN FREE PATH
Average distance a molecule travels between collisions.

6. LAW OF EQUIPARTITION OF ENERGY
Each degree of freedom contributes (1/2)kT to energy.

7. HEAT CAPACITY OF GASES
Cp – Cv = R  
γ = Cp / Cv

8. REAL GASES & DEVIATION
Real gases deviate at high pressure & low temperature.

9. VAN DER WAALS EQUATION
(P + a/V²)(V – b) = RT
""","Electricity": """

1. ELECTRIC CHARGE
• Like charges repel, unlike attract.
• SI unit: Coulomb (C)

2. COULOMB’S LAW
F = k q1 q2 / r²

3. ELECTRIC FIELD
E = F / q  
• Direction: away from +ve, towards -ve charge.

4. ELECTRIC POTENTIAL
Work done per unit charge.  
Unit: Volt

V = W/q

5. ELECTRIC POTENTIAL ENERGY
U = k q1 q2 / r

6. OHM’S LAW
V = IR

7. RESISTANCE
R = ρ L / A

8. SERIES & PARALLEL
Series: R_total = R1 + R2 + …  
Parallel: 1/R_total = 1/R1 + 1/R2 + …

9. ELECTRIC POWER
P = VI = I²R = V² / R

10. KIRCHHOFF’S LAWS
• Junction rule: sum of currents = 0  
• Loop rule: sum of potential differences = 0
""",

"Electricity": """
ELECTRICITY – CLASS 10/11 PHYSICS

1. ELECTRIC CHARGE
• Like charges repel, unlike attract.
• SI unit: Coulomb (C)

2. COULOMB’S LAW
F = k q1 q2 / r²

3. ELECTRIC FIELD
E = F / q  
• Direction: away from +ve, towards -ve charge.

4. ELECTRIC POTENTIAL
Work done per unit charge.  
Unit: Volt

V = W/q

5. ELECTRIC POTENTIAL ENERGY
U = k q1 q2 / r

6. OHM’S LAW
V = IR

7. RESISTANCE
R = ρ L / A

8. SERIES & PARALLEL
Series: R_total = R1 + R2 + …  
Parallel: 1/R_total = 1/R1 + 1/R2 + …

9. ELECTRIC POWER
P = VI = I²R = V² / R

10. KIRCHHOFF’S LAWS
• Junction rule: sum of currents = 0  
• Loop rule: sum of potential differences = 0
""","Magnetism": """
MAGNETISM – CLASS 11 PHYSICS

1. MAGNETIC FIELD
Region around a magnet where magnetic effects are felt.
Unit: Tesla (T)

2. MAGNETIC FIELD DUE TO CURRENT
Biot–Savart Law:
dB = (μ0 I dl sinθ) / (4πr²)

3. MAGNETIC FIELD OF STRAIGHT WIRE
B = μ0 I / (2πr)

4. FORCE ON MOVING CHARGE
F = q v B sinθ

5. FORCE ON CURRENT CARRYING WIRE
F = I L B sinθ

6. AMPERE’S CIRCUITAL LAW
∮ B dl = μ0 I

7. MAGNETIC MATERIALS
• Diamagnetic  
• Paramagnetic  
• Ferromagnetic

8. EARTH’S MAGNETISM
Earth behaves like a giant bar magnet.

9. ELECTROMAGNET
Produced by current through coils; strength ∝ current × turns.

10. SOLENOID FIELD
B = μ0 n I
""","Optics": """
OPTICS – CLASS 12 PHYSICS

1. REFLECTION OF LIGHT
• Follows laws: angle of incidence = angle of reflection.
• Mirrors: plane, concave, convex.

2. MIRROR FORMULA
1/f = 1/v + 1/u

3. LENSES
• Convex (converging)
• Concave (diverging)

4. LENS FORMULA
1/f = 1/v + 1/u

5. MAGNIFICATION
m = h'/h = v/u

6. TOTAL INTERNAL REFLECTION (TIR)
Occurs when:
• Light travels from denser → rarer medium.
• i > critical angle.

Applications: crystals, optical fibers.

7. REFRACTION
n = c / v  
Snell’s law: n1 sin i = n2 sin r

8. DISPERSION
Splitting of white light into seven colors.

9. OPTICAL INSTRUMENTS
• Microscope: high magnification using two lenses.
• Telescope: objective (large f), eyepiece (small f).

10. WAVE OPTICS
• Interference: constructive & destructive.
• Diffraction: bending around edges.
• Young’s double-slit experiment (YDSE): β = λD/d.

11. POLARISATION
Restricting vibrations of light to one plane.
""","Atoms": """
ATOMS – CLASS 12 PHYSICS

1. THOMSON MODEL
Plum pudding model: electrons embedded in positive sphere.

2. RUTHERFORD MODEL
• Mostly empty space.
• Positive charge concentrated in nucleus.
• Electrons revolve like planets.

3. BOHR’S MODEL
• Electrons revolve in quantized orbits.
• Angular momentum: mvr = n(h/2π).
• Energy levels: En = –13.6/n² eV.

4. RADIATION EMISSION
hf = Ei – Ef  
Photon emitted when electron jumps to lower orbit.

5. HYDROGEN SPECTRUM
Series: Lyman, Balmer, Paschen,…

6. DE BROGLIE WAVELENGTH
λ = h/p  
Particles have wave nature → standing waves in orbit.

7. ATOMIC MASS UNIT
1 u = 1.66 × 10^–27 kg
""","Nuclei": """
NUCLEI – CLASS 12 PHYSICS

1. COMPOSITION OF NUCLEUS
• Nucleons = protons + neutrons.
• A = mass number, Z = atomic number.

2. ISOTOPES, ISOBARS, ISOTONES
• Same Z, different A → isotopes.
• Same A → isobars.
• Same neutrons → isotones.

3. NUCLEAR FORCE
• Short range.
• Strongest force in nature.
• Charge independent.

4. MASS–ENERGY RELATION
E = mc²  
Mass defect → binding energy.

5. BINDING ENERGY PER NUCLEON
Explains stability of nuclei:
• Peaks at iron (Fe-56) → most stable.

6. RADIOACTIVITY
Types:
• Alpha decay (He nucleus)
• Beta decay (e⁻ or e⁺ emission)
• Gamma decay (high energy photon)

7. HALF-LIFE
Time taken for half the nuclei to decay.

8. NUCLEAR FISSION
• Heavy nucleus splits into two.
• Releases huge energy.
• Used in reactors.

9. NUCLEAR FUSION
• Light nuclei combine.
• Sun’s energy source.
• Requires high temperature.

10. CHAIN REACTION
Neutrons trigger further reactions.
""","EM Waves": """
ELECTROMAGNETIC WAVES – CLASS 12

1. ELECTROMAGNETIC WAVES
• Produced by accelerating charges.
• Electric and magnetic fields vary sinusoidally and are perpendicular to each other.

2. SPEED OF EM WAVES
c = 1 / √(μ₀ε₀)

3. NATURE OF EM WAVES
• Transverse waves
• Carry energy and momentum
• Do not require a medium

4. ELECTROMAGNETIC SPECTRUM (low to high frequency)
• Radio waves
• Microwaves
• Infrared
• Visible light
• Ultraviolet
• X-rays
• Gamma rays

5. POLARISATION
Only transverse waves can be polarised.

6. APPLICATIONS
• Radio waves → communication
• Microwaves → cooking, RADAR
• Infrared → night vision
• UV → sterilisation
• X-rays → imaging
• Gamma → cancer treatment
""","Dual Nature": """
DUAL NATURE OF RADIATION AND MATTER – CLASS 12

1. PHOTOELECTRIC EFFECT
• Light ejects electrons from metal surface.
• No electrons below threshold frequency.

2. EINSTEIN’S PHOTOELECTRIC EQUATION
hv = hv₀ + 1/2 mv²(max)

3. WORK FUNCTION
Minimum energy to eject electron.

4. DE BROGLIE WAVELENGTH
λ = h / p = h / mv

5. WAVE–PARTICLE DUALITY
• Light behaves as both wave and particle.
• Matter also has wave nature (electron diffraction).

6. EXPERIMENTS
• Davisson–Germer experiment confirmed electron waves.

7. EFFECT OF INTENSITY
• Intensity affects number of electrons, not energy.

8. EFFECT OF FREQUENCY
• Higher frequency → higher electron energy.

""","Semiconductors": """
SEMICONDUCTORS AND ELECTRONIC DEVICES – CLASS 12

1. TYPES OF MATERIALS
• Conductors → many free electrons.
• Insulators → no free electrons.
• Semiconductors → moderate conductivity (Si, Ge).

2. INTRINSIC & EXTRINSIC SEMICONDUCTORS
• Intrinsic → pure.
• Extrinsic → doped:
   – n-type → more electrons
   – p-type → more holes

3. P–N JUNCTION
• Diode formed by p-region and n-region.
• Forward bias → conducts
• Reverse bias → blocks

4. ZENER DIODE
• Used for voltage regulation.

5. TRANSISTORS (NPN/PNP)
• Three regions: emitter, base, collector.
• Used for switching & amplification.

6. LOGIC GATES
• AND, OR, NOT, NAND, NOR, XOR.

7. CHARACTERISTICS
• I–V curve of diode
• Breakdown voltage

8. RECTIFIERS
• Convert AC → DC
• Types: half-wave, full-wave, bridge rectifier

""","Communication": """
COMMUNICATION SYSTEMS – CLASS 12

1. ELEMENTS OF COMMUNICATION
• Transmitter → sends message
• Channel → medium
• Receiver → receives message

2. TYPES OF SIGNALS
• Analog → continuous
• Digital → discrete

3. MODULATION
Process of superimposing message on carrier wave.
• Amplitude modulation (AM)
• Frequency modulation (FM)
• Phase modulation (PM)

4. NEED FOR MODULATION
• Increase range
• Reduce noise
• Efficient transmission

5. BANDWIDTH
Frequency range of a signal.

6. ANTENNAS
• Used for transmission and reception
• Height depends on wavelength

7. PROPAGATION OF EM WAVES
• Ground wave
• Sky wave
• Space wave

8. NOISE
Undesired signals that distort communication.

9. SATELLITE COMMUNICATION
• Geostationary satellites
• Uplink & downlink frequencies

""",
}

quizqns ={"Kinematics": [
    {
        "q": "What physical quantity is measured by the slope of a distance-time graph?",
        "options": ["Speed", "Acceleration", "Displacement", "Force"],
        "answer": "Speed"
    },
    {
        "q": "What does the area under a velocity–time graph represent?",
        "options": ["Velocity", "Acceleration", "Displacement", "Speed"],
        "answer": "Displacement"
    },
    {
        "q": "Which of the following is a vector quantity?",
        "options": ["Speed", "Distance", "Displacement", "Time"],
        "answer": "Displacement"
    },
    {
        "q": "What is the SI unit of acceleration?",
        "options": ["m/s", "m/s²", "km/h", "N"],
        "answer": "m/s²"
    },
    {
        "q": "A body moves with constant velocity. What is its acceleration?",
        "options": ["Zero", "Constant", "Increasing", "Decreasing"],
        "answer": "Zero"
    },
    {
        "q": "Which equation of motion relates velocity, acceleration, and displacement?",
        "options": ["v = u + at", "s = ut + 1/2 at²", "v² = u² + 2as", "s = vt"],
        "answer": "v² = u² + 2as"
    },
    {
        "q": "What does negative acceleration represent?",
        "options": ["Increasing speed", "Decreasing speed", "Zero speed", "Constant speed"],
        "answer": "Decreasing speed"
    },
    {
        "q": "A body is thrown upward. What is its acceleration at the highest point?",
        "options": ["Zero", "g", "-g", "Infinity"],
        "answer": "-g"
    },
    {
        "q": "Which graph represents uniform motion?",
        "options": ["Straight line in distance-time graph", "Curved velocity-time graph", "Parabolic displacement-time graph", "Horizontal acceleration-time graph"],
        "answer": "Straight line in distance-time graph"
    },
    {
        "q": "What happens to velocity in uniform accelerated motion?",
        "options": ["Remains constant", "Changes uniformly", "Becomes zero", "Becomes negative"],
        "answer": "Changes uniformly"
    }
]
,"Newtons laws of motion": [
    {
        "q": "Which law explains inertia?",
        "options": ["Newton's 1st law", "Newton's 2nd law", "Newton's 3rd law", "Gravitation law"],
        "answer": "Newton's 1st law"
    },
    {
        "q": "Which law is represented by F = ma?",
        "options": ["Newton's 1st law", "Newton's 2nd law", "Newton's 3rd law", "Kepler's law"],
        "answer": "Newton's 2nd law"
    },
    {
        "q": "Action and reaction forces act on how many bodies?",
        "options": ["One body", "Two bodies", "Three bodies", "None"],
        "answer": "Two bodies"
    },
    {
        "q": "When a car stops suddenly and passengers move forward, which law applies?",
        "options": ["1st law", "2nd law", "3rd law", "Law of gravitation"],
        "answer": "1st law"
    },
    {
        "q": "What is the SI unit of force?",
        "options": ["kg", "m/s²", "N", "J"],
        "answer": "N"
    },
    {
        "q": "Which law states that an external force is required to change the state of motion?",
        "options": ["1st law", "2nd law", "3rd law", "4th law"],
        "answer": "1st law"
    },
    {
        "q": "What happens to acceleration if force is doubled and mass is constant?",
        "options": ["Becomes double", "Becomes half", "Becomes zero", "Remains same"],
        "answer": "Becomes double"
    },
    {
        "q": "Which law explains recoil of a gun?",
        "options": ["1st law", "2nd law", "3rd law", "Gravitation"],
        "answer": "3rd law"
    },
    {
        "q": "Which force opposes relative motion between two surfaces?",
        "options": ["Normal force", "Tension", "Friction", "Electrostatic force"],
        "answer": "Friction"
    },
    {
        "q": "What happens to acceleration when mass is doubled but force remains constant?",
        "options": ["Doubles", "Becomes half", "Becomes zero", "Becomes infinite"],
        "answer": "Becomes half"
    }
],'Work power and energy': [
    {
        "q": "What is the SI unit of work?",
        "options": ["Joule", "Watt", "Newton", "Pascal"],
        "answer": "Joule"
    },
    {
        "q": "Work done is zero when:",
        "options": ["Force is applied", "Displacement is zero", "Both force and displacement exist", "Force and displacement are perpendicular"],
        "answer": "Displacement is zero"
    },
    {
        "q": "Power is defined as:",
        "options": ["Work × Time", "Work / Time", "Force × Distance", "Energy × Time"],
        "answer": "Work / Time"
    },
    {
        "q": "What type of energy is stored in a stretched spring?",
        "options": ["Kinetic energy", "Potential energy", "Thermal energy", "Chemical energy"],
        "answer": "Potential energy"
    },
    {
        "q": "Kinetic energy depends on:",
        "options": ["Mass only", "Velocity only", "Mass and velocity", "Acceleration"],
        "answer": "Mass and velocity"
    },
    {
        "q": "Which formula represents kinetic energy?",
        "options": ["mgh", "1/2 mv²", "F × d", "P × t"],
        "answer": "1/2 mv²"
    },
    {
        "q": "If velocity of a body is doubled, its kinetic energy becomes:",
        "options": ["Double", "Half", "Four times", "Eight times"],
        "answer": "Four times"
    },
    {
        "q": "The unit of power is:",
        "options": ["J", "W", "N", "kg m/s"],
        "answer": "W"
    },
    {
        "q": "A man lifts a box and holds it still. Work done by him is:",
        "options": ["Positive", "Negative", "Zero", "Infinite"],
        "answer": "Zero"
    },
    {
        "q": "Which energy conversion happens in a falling object?",
        "options": ["Kinetic to potential", "Potential to kinetic", "Chemical to heat", "Electrical to mechanical"],
        "answer": "Potential to kinetic"
    }],"Rotation": [
    {
        "q": "Which quantity measures a body's resistance to rotational motion?",
        "options": ["Torque", "Moment of inertia", "Angular velocity", "Angular displacement"],
        "answer": "Moment of inertia"
    },
    {
        "q": "The SI unit of angular velocity is:",
        "options": ["radian", "radian/sec", "sec", "m/sec"],
        "answer": "radian/sec"
    },
    {
        "q": "Which relation is correct?",
        "options": ["v = rα", "v = rω", "ω = rv", "τ = mv"],
        "answer": "v = rω"
    },
    {
        "q": "Torque is equal to:",
        "options": ["Iα", "mv", "F/m", "ω/t"],
        "answer": "Iα"
    },
    {
        "q": "A solid disc and a ring roll down the same incline. Which reaches first?",
        "options": ["Ring", "Disc", "Both together", "Depends on mass"],
        "answer": "Disc"
    },
    {
        "q": "Rotational kinetic energy is given by:",
        "options": ["(1/2)mv²", "(1/2)Iω²", "Iω", "rF"],
        "answer": "(1/2)Iω²"
    },
    {
        "q": "Angular momentum L is equal to:",
        "options": ["I/ω", "Iω", "Fω", "ω/r"],
        "answer": "Iω"
    },
    {
        "q": "When no external torque acts on a system, which quantity is conserved?",
        "options": ["Angular displacement", "Angular momentum", "Torque", "Moment of inertia"],
        "answer": "Angular momentum"
    },
    {
        "q": "For pure rolling motion, which relation holds?",
        "options": ["v = ω/r", "v = Rω", "v = R/ω", "v = ω²R"],
        "answer": "v = Rω"
    },
    {
        "q": "Which object has the highest moment of inertia for the same mass and radius?",
        "options": ["Solid sphere", "Solid disc", "Hollow sphere", "Ring"],
        "answer": "Ring"
    }
],"Gravitation": [
    {
        "q": "What is the universal law of gravitation?",
        "options": [
            "F = G(m1m2)/r²",
            "F = ma",
            "P = F/A",
            "V = IR"
        ],
        "answer": "F = G(m1m2)/r²"
    },
    {
        "q": "What is the value of the universal gravitational constant (G)?",
        "options": [
            "9.8 m/s²",
            "6.67 × 10⁻¹¹ N m²/kg²",
            "3 × 10⁸ m/s",
            "1.6 × 10⁻¹⁹ C"
        ],
        "answer": "6.67 × 10⁻¹¹ N m²/kg²"
    },
    {
        "q": "Gravitational force is always:",
        "options": [
            "Repulsive",
            "Attractive",
            "Sometimes attractive",
            "Zero"
        ],
        "answer": "Attractive"
    },
    {
        "q": "The force of gravitation between two bodies depends on:",
        "options": [
            "Their masses and distance",
            "Only their masses",
            "Only their distance",
            "Their volume"
        ],
        "answer": "Their masses and distance"
    },
    {
        "q": "According to Newton's law, gravitational force is inversely proportional to:",
        "options": [
            "r",
            "r²",
            "m",
            "m²"
        ],
        "answer": "r²"
    },
    {
        "q": "Which quantity decreases with increase in height from Earth's surface?",
        "options": [
            "Gravitational acceleration (g)",
            "Gravitational constant (G)",
            "Mass of object",
            "Momentum"
        ],
        "answer": "Gravitational acceleration (g)"
    },
    {
        "q": "Which law states T² ∝ R³?",
        "options": [
            "Kepler's 1st law",
            "Kepler's 2nd law",
            "Kepler's 3rd law",
            "Newton’s law"
        ],
        "answer": "Kepler's 3rd law"
    },
    {
        "q": "Escape velocity for Earth is approximately:",
        "options": [
            "5 km/s",
            "11.2 km/s",
            "20 km/s",
            "3 km/s"
        ],
        "answer": "11.2 km/s"
    },
    {
        "q": "Gravitational potential energy is:",
        "options": [
            "Positive",
            "Negative",
            "Zero",
            "Undefined"
        ],
        "answer": "Negative"
    },
    {
        "q": "What happens to gravitational force if the distance between two masses is doubled?",
        "options": [
            "It becomes double",
            "It becomes half",
            "It becomes four times",
            "It becomes one-fourth"
        ],
        "answer": "It becomes one-fourth"
    }],"Centre of Mass and Collisions": [
    {
        "q": "Centre of mass of a system depends on:",
        "options": ["Mass distribution", "Shape only", "Volume only", "Density only"],
        "answer": "Mass distribution"
    },
    {
        "q": "For a uniform rod, the centre of mass lies at:",
        "options": ["One end", "Midpoint", "One-third length", "Varies"],
        "answer": "Midpoint"
    },
    {
        "q": "In which collision is kinetic energy conserved?",
        "options": ["Elastic", "Inelastic", "Perfectly inelastic", "Explosive"],
        "answer": "Elastic"
    },
    {
        "q": "Momentum in any collision is:",
        "options": ["Always conserved", "Never conserved", "Conserved only in elastic collisions", "Conserved only in inelastic collisions"],
        "answer": "Always conserved"
    },
    {
        "q": "If two bodies stick together after collision, the collision is:",
        "options": ["Elastic", "Inelastic", "Perfectly inelastic", "Explosive"],
        "answer": "Perfectly inelastic"
    },
    {
        "q": "Coefficient of restitution (e) for perfectly inelastic collision is:",
        "options": ["1", "0", "Between 0 and 1", "Greater than 1"],
        "answer": "0"
    },
    {
        "q": "The motion of centre of mass is affected by:",
        "options": ["External forces only", "Internal forces only", "Both internal and external forces", "No forces"],
        "answer": "External forces only"
    },
    {
        "q": "In an elastic head-on collision between equal masses, the bodies:",
        "options": ["Stick together", "Come to rest", "Exchange velocities", "Move in same direction"],
        "answer": "Exchange velocities"
    },
    {
        "q": "Which quantity is NOT conserved in an inelastic collision?",
        "options": ["Momentum", "Kinetic energy", "Mass", "Total energy"],
        "answer": "Kinetic energy"
    },
    {
        "q": "A bomb explodes into pieces. The centre of mass of the system:",
        "options": ["Moves randomly", "Remains at rest or moves uniformly", "Accelerates suddenly", "Disappears"],
        "answer": "Remains at rest or moves uniformly"
    }],'Thermodynamics' : [
    {
        "q": "What does the first law of thermodynamics state?",
        "options": [
            "Energy can be created",
            "Energy can be destroyed",
            "Energy is conserved",
            "Heat flows from cold to hot"
        ],
        "answer": "Energy is conserved"
    },
    {
        "q": "In an isothermal process, which quantity remains constant?",
        "options": ["Pressure", "Volume", "Temperature", "Entropy"],
        "answer": "Temperature"
    },
    {
        "q": "Which thermodynamic process occurs at constant volume?",
        "options": ["Isobaric", "Isothermal", "Isochoric", "Adiabatic"],
        "answer": "Isochoric"
    },
    {
        "q": "In an adiabatic process, what is the heat exchange?",
        "options": ["Positive", "Negative", "Zero", "Infinite"],
        "answer": "Zero"
    },
    {
        "q": "Which law is expressed as PV = nRT?",
        "options": ["Boyle’s Law", "Ideal Gas Law", "Charles’ Law", "Newton’s Law"],
        "answer": "Ideal Gas Law"
    },
    {
        "q": "What does entropy measure?",
        "options": ["Temperature", "Disorder", "Energy", "Pressure"],
        "answer": "Disorder"
    },
    {
        "q": "The efficiency of a heat engine is the ratio of:",
        "options": ["Work output to heat input", "Heat input to work output", "Heat lost to heat gained", "Volume to pressure"],
        "answer": "Work output to heat input"
    },
    {
        "q": "Which device transfers heat from a cold body to a hot body?",
        "options": ["Heat engine", "Turbine", "Refrigerator", "Generator"],
        "answer": "Refrigerator"
    },
    {
        "q": "Which quantity remains constant in an isobaric process?",
        "options": ["Pressure", "Volume", "Temperature", "Mass"],
        "answer": "Pressure"
    },
    {
        "q": "What is the SI unit of heat?",
        "options": ["Newton", "Joule", "Watt", "Pascal"],
        "answer": "Joule"
    }


],"Mechanical Properties of Solids": [
        {
            "q": "What is the property of a body to regain its original shape after deformation?",
            "options": ["Plasticity", "Elasticity", "Rigidity", "Viscosity"],
            "answer": "Elasticity"
        },
        {
            "q": "Which law relates stress and strain?",
            "options": ["Newton’s law", "Hooke’s law", "Boyle’s law", "Kepler’s law"],
            "answer": "Hooke’s law"
        },
        {
            "q": "What is the SI unit of stress?",
            "options": ["Pascal", "Newton", "Joule", "Watt"],
            "answer": "Pascal"
        },
        {
            "q": "Young’s modulus is defined for which type of deformation?",
            "options": ["Shear", "Bulk", "Tensile/Longitudinal", "Thermal"],
            "answer": "Tensile/Longitudinal"
        },
        {
            "q": "Which quantity is defined as force per unit area?",
            "options": ["Strain", "Stress", "Pressure", "Elastic limit"],
            "answer": "Stress"
        },
        {
            "q": "Permanent deformation of a solid is called:",
            "options": ["Elasticity", "Plasticity", "Strain", "Ductility"],
            "answer": "Plasticity"
        },
        {
            "q": "Breaking stress of a material is called:",
            "options": ["Elastic limit", "Yield point", "Ultimate tensile strength", "Plastic limit"],
            "answer": "Ultimate tensile strength"
        },
        {
            "q": "The ratio of lateral strain to longitudinal strain is:",
            "options": ["Young’s modulus", "Shear modulus", "Poisson’s ratio", "Bulk modulus"],
            "answer": "Poisson’s ratio"
        },
        {
            "q": "Which solid has the highest Young’s modulus?",
            "options": ["Glass", "Rubber", "Steel", "Copper"],
            "answer": "Steel"
        },
        {
            "q": "Bulk modulus describes change in:",
            "options": ["Shape only", "Volume only", "Length only", "Mass only"],
            "answer": "Volume only"
        }
    ],

    "Mechanical Properties of Fluids": [
        {
            "q": "What is defined as force per unit area in fluids?",
            "options": ["Stress", "Pressure", "Strain", "Viscosity"],
            "answer": "Pressure"
        },
        {
            "q": "Which law states that pressure applied to a fluid is transmitted equally in all directions?",
            "options": ["Archimedes’ principle", "Pascal’s law", "Bernoulli’s principle", "Hooke’s law"],
            "answer": "Pascal’s law"
        },
        {
            "q": "Which principle explains why objects float?",
            "options": ["Bernoulli’s principle", "Pascal’s law", "Archimedes’ principle", "Hooke’s law"],
            "answer": "Archimedes’ principle"
        },
        {
            "q": "The upward force acting on a submerged object is called:",
            "options": ["Viscous force", "Buoyant force", "Drag force", "Lift force"],
            "answer": "Buoyant force"
        },
        {
            "q": "Viscosity is the measure of:",
            "options": ["Elasticity", "Resistance to flow", "Density", "Pressure"],
            "answer": "Resistance to flow"
        },
        {
            "q": "Which liquid has the highest viscosity?",
            "options": ["Water", "Alcohol", "Honey", "Milk"],
            "answer": "Honey"
        },
        {
            "q": "Bernoulli’s principle is based on the conservation of:",
            "options": ["Mass", "Energy", "Momentum", "Charge"],
            "answer": "Energy"
        },
        {
            "q": "Pressure in a fluid increases with:",
            "options": ["Height", "Temperature", "Depth", "Velocity"],
            "answer": "Depth"
        },
        {
            "q": "An ideal fluid has:",
            "options": ["Zero viscosity", "Zero density", "Zero pressure", "Zero mass"],
            "answer": "Zero viscosity"
        },
        {
            "q": "SI unit of viscosity is:",
            "options": ["Pa", "Pa·s", "N·m", "kg/m³"],
            "answer": "Pa·s"
        }
    ],"SHM": [
    {
        "q": "Which force is responsible for Simple Harmonic Motion?",
        "options": ["Constant force", "Resistive force", "Restoring force", "Gravitational force"],
        "answer": "Restoring force"
    },
    {
        "q": "Which equation represents displacement in SHM?",
        "options": ["x = vt", "x = A sin(ωt + φ)", "x = ut + 1/2 at²", "x = A + Bt"],
        "answer": "x = A sin(ωt + φ)"
    },
    {
        "q": "Velocity of the particle in SHM is maximum at:",
        "options": ["Mean position", "Extreme position", "Midway position", "Always constant"],
        "answer": "Mean position"
    },
    {
        "q": "Acceleration in SHM is maximum at:",
        "options": ["Mean position", "Extreme position", "Both positions", "None"],
        "answer": "Extreme position"
    },
    {
        "q": "Which of the following is true about total energy in SHM?",
        "options": ["Increases", "Decreases", "Constant", "Zero"],
        "answer": "Constant"
    },
    {
        "q": "Time period of a spring-mass system is:",
        "options": ["2π √(m/k)", "2π √(k/m)", "m/k", "k/m"],
        "answer": "2π √(m/k)"
    },
    {
        "q": "Angular frequency ω equals:",
        "options": ["√(k/m)", "k/m", "2πm", "A/k"],
        "answer": "√(k/m)"
    },
    {
        "q": "At mean position in SHM, acceleration is:",
        "options": ["Maximum", "Minimum", "Zero", "Negative"],
        "answer": "Zero"
    },
    {
        "q": "Which quantity remains constant in SHM?",
        "options": ["Displacement", "Velocity", "Acceleration", "Total energy"],
        "answer": "Total energy"
    },
    {
        "q": "The restoring force in SHM is proportional to:",
        "options": ["Velocity", "Time", "Displacement", "Mass"],
        "answer": "Displacement"
    }
],"Waves": [
    {
        "q": "Which of the following is a mechanical wave?",
        "options": ["Light", "Radio wave", "Sound", "X-ray"],
        "answer": "Sound"
    },
    {
        "q": "In a transverse wave, particles vibrate:",
        "options": ["Along the direction of propagation", "Perpendicular to propagation", "Randomly", "Not at all"],
        "answer": "Perpendicular to propagation"
    },
    {
        "q": "Wave speed is given by:",
        "options": ["v = λ/T", "v = fλ", "v = f/T", "v = Aλ"],
        "answer": "v = fλ"
    },
    {
        "q": "The time period of a wave is:",
        "options": ["T = 1/f", "T = fλ", "T = λ/v", "T = Av"],
        "answer": "T = 1/f"
    },
    {
        "q": "Standing waves are produced by:",
        "options": ["Two perpendicular waves", "Two waves travelling in same direction", "Two identical waves in opposite directions", "One stationary and one moving wave"],
        "answer": "Two identical waves in opposite directions"
    },
    {
        "q": "Which phenomenon explains large oscillations at natural frequency?",
        "options": ["Diffraction", "Resonance", "Reflection", "Polarisation"],
        "answer": "Resonance"
    },
    {
        "q": "Wavelength is the distance between:",
        "options": ["Two troughs", "Two crests", "Any two identical points", "All of the above"],
        "answer": "All of the above"
    },
    {
        "q": "Which quantity remains constant when a wave enters a new medium?",
        "options": ["Wavelength", "Speed", "Frequency", "Amplitude"],
        "answer": "Frequency"
    },
    {
        "q": "Superposition principle states:",
        "options": ["Waves reflect always", "Resultant displacement is sum of individual displacements", "Waves disappear after collision", "Amplitude becomes zero always"],
        "answer": "Resultant displacement is sum of individual displacements"
    },
    {
        "q": "Which wave does NOT require a medium?",
        "options": ["Sound", "Water wave", "Light", "Seismic wave"],
        "answer": "Light"
    }
],"Kinetic Theory": [
    {
        "q": "According to kinetic theory, pressure of a gas is due to:",
        "options": ["Intermolecular forces", "Collision of molecules with walls", "Gravity", "Temperature differences"],
        "answer": "Collision of molecules with walls"
    },
    {
        "q": "RMS speed of gas molecules is proportional to:",
        "options": ["√T", "T", "1/T", "1/√T"],
        "answer": "√T"
    },
    {
        "q": "Which relation is correct?",
        "options": ["Cp – Cv = T", "Cp + Cv = R", "Cp – Cv = R", "Cp / Cv = R"],
        "answer": "Cp – Cv = R"
    },
    {
        "q": "Van der Waals constant 'a' accounts for:",
        "options": ["Volume of molecules", "Attractive forces", "Temperature", "Shape"],
        "answer": "Attractive forces"
    },
    {
        "q": "For a monoatomic gas, γ is:",
        "options": ["1.4", "1.67", "2.0", "1.2"],
        "answer": "1.67"
    },
    {
        "q": "Mean free path is:",
        "options": ["Distance between molecules", "Distance between collisions", "Height of container", "Speed of gas"],
        "answer": "Distance between collisions"
    },
    {
        "q": "Ideal gas molecules have:",
        "options": ["Strong forces", "Weak attractive forces", "No intermolecular forces", "Repulsive forces"],
        "answer": "No intermolecular forces"
    },
    {
        "q": "Internal energy of ideal gas depends only on:",
        "options": ["Pressure", "Volume", "Temperature", "Density"],
        "answer": "Temperature"
    },
    {
        "q": "The equation for RMS speed is:",
        "options": ["√(2RT/M)", "√(3RT/M)", "RT/M", "√(RT/2M)"],
        "answer": "√(3RT/M)"
    },
    {
        "q": "If temperature doubles, v_rms becomes:",
        "options": ["Double", "Half", "√2 times", "4 times"],
        "answer": "√2 times"
    }
],"Electricity": [
    {
        "q": "Unit of electric charge is:",
        "options": ["Newton", "Volt", "Coulomb", "Ohm"],
        "answer": "Coulomb"
    },
    {
        "q": "Electric field is:",
        "options": ["Force per unit charge", "Work per unit mass", "Charge per unit area", "Energy per volt"],
        "answer": "Force per unit charge"
    },
    {
        "q": "According to Ohm's law:",
        "options": ["I = VR", "V = IR", "R = IV", "P = I/R"],
        "answer": "V = IR"
    },
    {
        "q": "In series combination, resistance:",
        "options": ["Increases", "Decreases", "Becomes zero", "Doubles always"],
        "answer": "Increases"
    },
    {
        "q": "Power can be written as:",
        "options": ["P = I²R", "P = V/R", "P = IR²", "P = I/V"],
        "answer": "P = I²R"
    },
    {
        "q": "Electric potential is measured in:",
        "options": ["Ampere", "Watt", "Volt", "Joule"],
        "answer": "Volt"
    },
    {
        "q": "Coulomb’s law force is:",
        "options": ["Proportional to r²", "Inversely proportional to r²", "Independent of distance", "Proportional to r"],
        "answer": "Inversely proportional to r²"
    },
    {
        "q": "Current is:",
        "options": ["Charge × time", "Charge / time", "Voltage / resistance", "Resistance × charge"],
        "answer": "Charge / time"
    },
    {
        "q": "Which is a conductor?",
        "options": ["Rubber", "Glass", "Copper", "Wood"],
        "answer": "Copper"
    },
    {
        "q": "SI unit of resistance:",
        "options": ["Joule", "Watt", "Ohm", "Tesla"],
        "answer": "Ohm"
    }
],"Magnetism": [
    {
        "q": "Unit of magnetic field is:",
        "options": ["Ampere", "Tesla", "Weber", "Newton"],
        "answer": "Tesla"
    },
    {
        "q": "Magnetic field around a straight current-carrying wire is:",
        "options": ["Radial", "Circular", "Linear", "Irregular"],
        "answer": "Circular"
    },
    {
        "q": "Force on a moving charge is:",
        "options": ["qv", "qvB", "qvB sinθ", "q/B"],
        "answer": "qvB sinθ"
    },
    {
        "q": "Ferromagnetic material example:",
        "options": ["Wood", "Copper", "Iron", "Glass"],
        "answer": "Iron"
    },
    {
        "q": "Magnetic field of a solenoid is:",
        "options": ["Zero", "Weak", "Uniform", "Random"],
        "answer": "Uniform"
    },
    {
        "q": "Earth’s magnetism is due to:",
        "options": ["Molten core currents", "Rocks", "Air", "Gravity"],
        "answer": "Molten core currents"
    },
    {
        "q": "Magnetic field at center of circular loop is proportional to:",
        "options": ["I", "1/I", "I²", "1/r²"],
        "answer": "I"
    },
    {
        "q": "Force on a stationary charge in magnetic field is:",
        "options": ["Maximum", "Minimum", "Zero", "Infinite"],
        "answer": "Zero"
    },
    {
        "q": "Electromagnets work on:",
        "options": ["Static charges", "Flowing current", "Heat", "Light"],
        "answer": "Flowing current"
    },
    {
        "q": "Diamagnetic materials are:",
        "options": ["Strongly attracted", "Weakly attracted", "Weakly repelled", "Strongly repelled"],
        "answer": "Weakly repelled"
    }
],"Optics": [
    {
        "q": "Lens formula is:",
        "options": ["1/f = 1/v − 1/u", "1/f = 1/v + 1/u", "f = uv", "1/f = uv"],
        "answer": "1/f = 1/v + 1/u"
    },
    {
        "q": "TIR occurs when light travels from:",
        "options": ["Rarer to denser", "Denser to rarer", "Vacuum to glass", "Air to vacuum"],
        "answer": "Denser to rarer"
    },
    {
        "q": "Young’s double-slit fringe width is:",
        "options": ["β = dD/λ", "β = λD/d", "β = λd/D", "β = Dλ"],
        "answer": "β = λD/d"
    },
    {
        "q": "Refraction law is:",
        "options": ["Snell's law", "Ampere's law", "Faraday's law", "Newton's law"],
        "answer": "Snell's law"
    },
    {
        "q": "Magnification is:",
        "options": ["h/h'", "v/u", "h'/h", "uv"],
        "answer": "h'/h"
    }
],"Atoms": [
    {
        "q": "Bohr’s quantization rule is:",
        "options": ["mv = nh", "mvr = n(h/2π)", "mvr = n²h", "v = nh"],
        "answer": "mvr = n(h/2π)"
    },
    {
        "q": "Energy of nth orbit of hydrogen is:",
        "options": ["−13.6/n", "−13.6n²", "−13.6/n²", "13.6n"],
        "answer": "−13.6/n²"
    },
    {
        "q": "Rutherford discovered that:",
        "options": ["Electrons have waves", "Atom is mostly empty", "Charge is quantized", "Mass = energy"],
        "answer": "Atom is mostly empty"
    },
    {
        "q": "Photon energy is:",
        "options": ["hf", "h/f", "hf²", "1/hf"],
        "answer": "hf"
    },
    {
        "q": "de Broglie wavelength formula:",
        "options": ["λ = h/mv", "λ = mv/h", "λ = hm/v", "λ = mv"],
        "answer": "λ = h/mv"
    }
],"Nuclei": [
    {
        "q": "Binding energy is due to:",
        "options": ["Mass defect", "Charge", "Gravity", "Heat"],
        "answer": "Mass defect"
    },
    {
        "q": "Most stable nucleus is:",
        "options": ["Uranium-235", "Hydrogen", "Iron-56", "Helium-4"],
        "answer": "Iron-56"
    },
    {
        "q": "Half-life is:",
        "options": ["Time to double nuclei", "Time for half atoms to decay", "Time for fusion", "Time for fission"],
        "answer": "Time for half atoms to decay"
    },
    {
        "q": "Alpha particle is:",
        "options": ["Electron", "Helium nucleus", "Proton", "Neutron"],
        "answer": "Helium nucleus"
    },
    {
        "q": "Fusion is:",
        "options": ["Breaking heavy nucleus", "Combining light nuclei", "Electron capture", "Neutron absorption"],
        "answer": "Combining light nuclei"
    }
],"EM Waves": [
    {
        "q": "EM waves are produced by:",
        "options": ["Static charges", "Accelerating charges", "Heat", "Sound"],
        "answer": "Accelerating charges"
    },
    {
        "q": "EM waves are:",
        "options": ["Longitudinal", "Transverse", "Both", "Neither"],
        "answer": "Transverse"
    },
    {
        "q": "Speed of EM waves is:",
        "options": ["3×10⁶ m/s", "3×10⁸ m/s", "3×10¹⁰ m/s", "3×10⁴ m/s"],
        "answer": "3×10⁸ m/s"
    },
    {
        "q": "Radio waves have:",
        "options": ["Highest frequency", "Lowest frequency", "Shortest wavelength", "Highest energy"],
        "answer": "Lowest frequency"
    },
    {
        "q": "Polarisation occurs only in:",
        "options": ["Longitudinal waves", "Transverse waves", "Sound waves", "Shock waves"],
        "answer": "Transverse waves"
    }
],"Dual Nature": [
    {
        "q": "Photoelectric effect proves:",
        "options": ["Wave nature", "Particle nature", "Both", "None"],
        "answer": "Particle nature"
    },
    {
        "q": "de Broglie wavelength is:",
        "options": ["λ = mv", "λ = h/mv", "λ = hm/v", "λ = v/h"],
        "answer": "λ = h/mv"
    },
    {
        "q": "Einstein’s equation is:",
        "options": ["hv = 1/2mv²", "hv = hv₀ + 1/2mv²(max)", "E = mc²", "p = mv"],
        "answer": "hv = hv₀ + 1/2mv²(max)"
    },
    {
        "q": "Work function is:",
        "options": ["Energy of electron", "Minimum energy to remove electron", "K.E. of photon", "Frequency of light"],
        "answer": "Minimum energy to remove electron"
    },
    {
        "q": "Electron diffraction confirms:",
        "options": ["Particle nature", "Wave nature", "Magnetic nature", "None"],
        "answer": "Wave nature"
    }
],"Semiconductors": [
    {
        "q": "Doping increases:",
        "options": ["Bandgap", "Resistivity", "Conductivity", "Resistance"],
        "answer": "Conductivity"
    },
    {
        "q": "In n-type semiconductor, majority carriers are:",
        "options": ["Holes", "Electrons", "Protons", "Neutrons"],
        "answer": "Electrons"
    },
    {
        "q": "Forward bias means:",
        "options": ["P to negative, N to positive", "P to positive, N to negative", "Reverse polarity", "No current"],
        "answer": "P to positive, N to negative"
    },
    {
        "q": "Which device regulates voltage?",
        "options": ["Transistor", "Zener diode", "LED", "Photodiode"],
        "answer": "Zener diode"
    },
    {
        "q": "Logic gate giving output 0 only when both inputs 1:",
        "options": ["OR", "AND", "NAND", "NOT"],
        "answer": "NAND"
    }
],"Communication": [
    {
        "q": "Modulation is needed to:",
        "options": ["Increase power", "Increase range", "Reduce processing", "Change antenna"],
        "answer": "Increase range"
    },
    {
        "q": "AM stands for:",
        "options": ["Amplitude Modulation", "Audio Modulation", "Analog Message", "Antenna Mode"],
        "answer": "Amplitude Modulation"
    },
    {
        "q": "Digital signals are:",
        "options": ["Continuous", "Discrete", "Random", "Sinusoidal"],
        "answer": "Discrete"
    },
    {
        "q": "Sky wave propagation uses:",
        "options": ["Ionosphere", "Stratosphere", "Troposphere", "Exosphere"],
        "answer": "Ionosphere"
    },
    {
        "q": "Satellite communication uses:",
        "options": ["Ground waves", "Sky waves", "Geostationary orbits", "Underground cables"],
        "answer": "Geostationary orbits"
    }
],











}

if __name__ == '__main__':
    app.run(debug=True)
    