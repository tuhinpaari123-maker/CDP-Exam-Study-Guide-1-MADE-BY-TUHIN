"""
CDP Exam Practice Quiz: Domain 1 - Decarbonization Drivers
Python 3 + Tkinter only. No third-party packages required.

Run:
    python cdp_domain1_quiz.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

# Each item: (competency, question, four options, correct option index, explanation)
RAW_QUESTIONS = [
("1.1 Climate drivers", "A facility's cooling demand rises sharply during longer, hotter summers. Which response best addresses both operational emissions and future climate exposure?",
 ["Increase cooling setpoints without checking comfort or health impacts", "Combine load reduction, efficient cooling, electrification where feasible, and heat-risk planning", "Install a larger chiller and leave controls unchanged", "Purchase offsets before assessing building performance"], 1,
 "A combined strategy reduces loads and equipment emissions while planning for the hotter conditions that are already affecting operations."),
("1.1 Climate drivers", "A design team uses only historical weather files to size HVAC equipment for a building expected to operate for 40 years. What is the key weakness?",
 ["Historical weather is always more conservative than future weather", "It may not represent future heat, humidity, and extreme-weather conditions over the asset life", "It automatically overestimates renewable-energy output", "It prevents the use of energy modelling"], 1,
 "Long-lived assets should consider future climate projections and appropriate stress scenarios, not only historical averages."),
("1.1 Climate drivers", "During a heatwave, a building's peak electrical demand and cooling costs increase together. Which measure most directly reduces the underlying cooling load?",
 ["Add more plug loads during the afternoon", "Improve solar control, insulation, airtightness, and internal-load management", "Disable all ventilation regardless of indoor conditions", "Rely exclusively on emergency generators"], 1,
 "Envelope improvements and load management reduce heat gains, lowering cooling energy and often peak demand."),
("1.1 Climate drivers", "A coastal office faces rising humidity and more frequent intense rainfall. Which assessment is most appropriate for its building systems?",
 ["Assess only annual average outdoor temperature", "Assess moisture control, envelope water entry, drainage, corrosion, and HVAC latent loads", "Assess only lighting power density", "Assume the HVAC system will compensate for every envelope failure"], 1,
 "Coastal climate exposure can affect moisture, water intrusion, corrosion, and the energy needed to remove latent heat."),
("1.1 Climate drivers", "A facility's cooling plant performs poorly during extreme heat. What should the team examine first before selecting replacement equipment?",
 ["Only the equipment's nameplate capacity", "Peak and part-load performance, design conditions, controls, heat rejection, and future weather", "The colour of the plant-room walls", "Only the lowest first-cost quotation"], 1,
 "System performance depends on design conditions, controls, heat rejection, and part-load operation as well as nominal capacity."),
("1.1 Climate drivers", "Why can a warmer climate increase both water and energy stress at a building?",
 ["Cooling towers and irrigation may need more water while cooling systems use more energy", "Warmer weather eliminates all water demand", "Water use and energy use cannot affect one another", "Warmer weather always reduces cooling demand"], 0,
 "Heat can increase cooling and irrigation demand; water-intensive cooling can also create operational vulnerabilities."),
("1.1 Climate drivers", "A building is experiencing more frequent smoke events from regional wildfires. Which operational approach best balances health, resilience, and energy?",
 ["Turn off filtration to reduce fan energy in every circumstance", "Use an indoor-air-quality plan with appropriate filtration, pressure strategy, monitoring, and safe ventilation controls", "Keep outdoor air dampers fully open regardless of outdoor air quality", "Seal the building permanently and stop monitoring CO2"], 1,
 "Smoke events require a planned balance between outdoor-air exposure, filtration, pressure, and indoor air-quality monitoring."),
("1.1 Climate drivers", "An energy model predicts annual savings but does not model extreme heat or outages. What important risk could be missed?",
 ["Whether the building can maintain critical services during severe conditions", "Whether annual utility bills have units", "Whether the building has a postal address", "Whether occupants use furniture"], 0,
 "Annual energy modelling alone does not establish resilience during extreme events or grid interruptions."),
("1.1 Climate drivers", "Which statement best distinguishes climate mitigation from climate adaptation in building planning?",
 ["Mitigation reduces emissions; adaptation reduces harm from climate impacts", "Mitigation means emergency response only; adaptation means buying offsets", "They are interchangeable terms", "Adaptation always increases emissions and cannot be combined with mitigation"], 0,
 "Mitigation addresses causes by reducing greenhouse-gas emissions; adaptation prepares for and reduces impacts."),
("1.1 Climate drivers", "A building is electrifying heating. Which climate-related consideration is most important for a robust long-term decision?",
 ["Ignore grid emissions and future peak loads", "Evaluate efficiency, grid carbon trajectory, peak demand, backup needs, and future climate conditions", "Select equipment based only on appearance", "Assume electrification removes every resilience risk"], 1,
 "Electrification can reduce direct emissions, but grid emissions, demand peaks, and continuity of service still matter."),
("1.1 Climate drivers", "A data centre's cooling system is exposed to increasingly frequent extreme-heat days. Which metric is most useful alongside annual energy use?",
 ["Peak cooling capacity and performance under design extreme conditions", "Number of meeting rooms", "Annual landscaping spend only", "The number of exterior doors"], 0,
 "Critical facilities need performance metrics that test whether cooling remains adequate under extreme conditions."),
("1.1 Climate drivers", "Why should humidity projections be considered when evaluating future HVAC performance?",
 ["Humidity affects latent cooling loads, condensation risk, and occupant comfort", "Humidity only changes the colour of equipment", "Humidity has no relationship to HVAC systems", "Humidity projections replace all energy analysis"], 0,
 "Humidity influences moisture removal, comfort, and the risk of condensation and mould."),
("1.1 Climate drivers", "A facility manager proposes setting every thermostat much lower during a heatwave. What is the strongest critique?",
 ["Lower setpoints always reduce energy use", "It may increase peak demand and energy use without fixing envelope, controls, or equipment constraints", "It guarantees resilience during a blackout", "It removes the need for maintenance"], 1,
 "Aggressive setpoints can raise energy use and peak demand; load reduction and system optimisation are usually more robust."),
("1.1 Climate drivers", "Which scenario is the clearest example of a climate-driven operational risk?",
 ["A new reporting template is introduced", "A heatwave causes cooling equipment to derate just as occupant cooling demand peaks", "A tenant changes its logo", "A procurement team changes its meeting schedule"], 1,
 "The risk arises directly from a climate hazard affecting equipment capability and building demand."),
("1.1 Climate drivers", "A site is exposed to both drought and heat. Which planning choice is most defensible?",
 ["Select water- and energy-intensive cooling without evaluating alternatives", "Evaluate water availability, cooling technology, heat exposure, and critical-load requirements together", "Plan only for average rainfall", "Treat water supply as unrelated to cooling resilience"], 1,
 "Heat and drought can compound each other, so cooling, water, and energy dependencies should be assessed together."),
("1.1 Climate drivers", "What is the main reason to test a building's energy strategy against multiple climate scenarios?",
 ["One scenario guarantees an exact future forecast", "Different plausible futures reveal sensitivities and reduce dependence on a single assumption", "Scenarios remove uncertainty completely", "Scenarios are useful only after a failure"], 1,
 "Scenario analysis does not predict the future exactly; it helps test decisions across plausible conditions."),
("1.1 Climate drivers", "A building has efficient equipment but frequent overheating in perimeter offices. Which conclusion is best?",
 ["Efficient equipment proves that thermal comfort is adequate", "Controls, solar gains, zoning, envelope performance, and actual occupant conditions need investigation", "The only solution is to increase equipment size", "Comfort is unrelated to decarbonization"], 1,
 "Energy efficiency and comfort are related but not identical; the causes of local overheating should be diagnosed."),
("1.1 Climate drivers", "A facility wants to reduce emissions while preparing for more cooling-degree days. Which sequence is strongest?",
 ["Forecast loads, reduce demand, right-size efficient systems, then plan low-carbon supply and resilience", "Install the largest available plant first and assess loads later", "Ignore controls and focus on offsets", "Delay all work until climate forecasts are certain"], 0,
 "A demand-first sequence can avoid oversizing and supports efficient, low-carbon, resilient system design."),
("1.1 Climate drivers", "A hospital relies on uninterrupted cooling for critical spaces. Which climate risk response is most appropriate?",
 ["Treat all spaces as equally critical", "Identify critical cooling loads, failure modes, redundancy, backup power, and safe operating limits", "Use annual energy intensity as the only resilience measure", "Remove alarms to avoid nuisance notifications"], 1,
 "Critical services require consequence-based planning, redundancy where justified, and verified continuity arrangements."),
("1.1 Climate drivers", "A facility's roof membrane and electrical equipment are both vulnerable to intense rainfall. What does this illustrate?",
 ["Climate hazards can affect multiple building systems at once", "Only HVAC equipment is climate-sensitive", "Rainfall is always a minor operational issue", "Separate departments need not coordinate"], 0,
 "A single hazard can create cascading or correlated failures across the envelope and electrical systems."),

("1.1 Climate drivers", "A site is mapping climate hazards. Which combination is the most complete starting point for a building in a hot, flood-prone region?",
 ["Heat, flooding, extreme rainfall, humidity, and service interruptions", "Only average annual temperature", "Only the cost of cleaning", "Only the age of interior finishes"], 0,
 "A useful screening considers relevant acute events and chronic shifts, including secondary service impacts."),
("1.1 Climate drivers", "Which is an example of a physical climate risk rather than a transition risk?",
 ["A new carbon price increases operating costs", "A flood damages electrical switchgear and interrupts operations", "A lender changes its ESG questionnaire", "A client requires a low-carbon disclosure"], 1,
 "Physical risks arise from climate hazards and changing climate conditions; policy and market shifts are transition risks."),
("1.1 Climate drivers", "A building's emergency plan covers fire but not prolonged heat or grid outages. What is the best next step?",
 ["Assume existing procedures cover every hazard", "Conduct a climate-informed risk and business-continuity assessment with roles, triggers, and recovery plans", "Buy a larger boiler without a risk review", "Wait for an actual outage to define responsibilities"], 1,
 "A climate-informed continuity plan identifies hazards, dependencies, decision triggers, responsibilities, and recovery needs."),
("1.1 Climate drivers", "Which adaptation measure can also support mitigation when properly designed?",
 ["Shading that reduces solar heat gain and cooling energy", "A diesel generator running continuously without need", "Removing insulation from the roof", "Increasing uncontrolled air leakage"], 0,
 "External shading can reduce cooling demand, providing both adaptation benefits and lower operational emissions."),
("1.1 Climate drivers", "A site proposes flood barriers but leaves critical electrical equipment at ground level. What is the principal concern?",
 ["The barrier colour may not match the building", "Residual flood risk and equipment vulnerability may remain if water exceeds or bypasses the barrier", "Flood barriers always eliminate all risk", "Electrical equipment cannot be affected by water"], 1,
 "Risk controls should account for residual risk, exceedance, access, drainage, and the location of critical equipment."),
("1.1 Climate drivers", "Why should climate risk be assessed over the expected life of a major building asset?",
 ["Climate hazards and operating conditions can change substantially over that period", "Only the first year affects capital decisions", "Asset life is unrelated to climate", "Long-term assessment guarantees no failures"], 0,
 "Long-lived assets can face materially different conditions later in their service life."),
("1.1 Climate drivers", "A resilience project is being prioritised. Which method best supports transparent prioritisation?",
 ["Rank hazards by media attention alone", "Evaluate likelihood, consequence, exposure, vulnerability, criticality, and cost-effective risk reduction", "Choose the most visible equipment", "Fund only measures with immediate energy savings"], 1,
 "A structured risk method connects hazard likelihood and consequences with vulnerability and mitigation effectiveness."),
("1.1 Climate drivers", "A building uses on-site solar but has no storage or islanding capability. During a grid outage, what should the owner assume?",
 ["The solar system will always power the building", "Grid-tied solar may shut down during an outage unless designed and equipped for safe islanded operation", "Solar panels automatically power every critical load", "The building has no electrical risk"], 1,
 "Most ordinary grid-tied PV systems shut down during outages for safety unless specific islanding and control capabilities are provided."),
("1.1 Climate drivers", "What is the best way to treat uncertainty in local climate projections for a major retrofit?",
 ["Ignore it and use a single historical average", "Use credible scenarios, document assumptions, test sensitivities, and favour flexible or no-regret measures where appropriate", "Assume the most extreme imaginable event is certain", "Postpone every decision indefinitely"], 1,
 "Transparent scenario and sensitivity analysis helps avoid false precision and identifies robust choices."),
("1.1 Climate drivers", "A building has flood exposure, but the owner only considers average annual energy savings in its business case. What is missing?",
 ["Potential avoided downtime, damage, safety consequences, recovery costs, and continuity benefits", "A second calculation of the building's floor area only", "The colour of the flood map", "Nothing; energy savings capture all resilience value"], 0,
 "Resilience benefits often include avoided losses and continuity of operations, not just utility savings."),
("1.1 Climate drivers", "Which measure best reduces the risk that extreme heat makes a naturally ventilated building unusable?",
 ["Rely on natural ventilation under every outdoor condition", "Evaluate overheating, shaded openings, night cooling, thermal mass, safe limits, and backup cooling needs", "Remove all external shading", "Close every window permanently without ventilation planning"], 1,
 "Passive measures can help, but performance must be assessed against future outdoor conditions and safe comfort limits."),
("1.1 Climate drivers", "A facility depends on municipal water for cooling, and the region faces drought restrictions. What is the most useful resilience question?",
 ["Can the building maintain safe critical operations under plausible water restrictions?", "Can the building change its name?", "Is the lobby lighting decorative?", "Can the facility stop recording utility data?"], 0,
 "Dependency analysis should test how reduced water availability affects critical functions and what alternatives exist."),
("1.1 Climate drivers", "Which statement about climate risk and energy efficiency is most accurate?",
 ["An efficient building is automatically resilient to every climate hazard", "Efficiency can lower loads, but resilience also requires hazard-specific design, redundancy, and continuity planning", "Efficiency always worsens resilience", "Resilience and energy use are completely unrelated"], 1,
 "Efficiency is valuable but does not, by itself, address flood, outage, smoke, water, or other hazard-specific risks."),
("1.1 Climate drivers", "A retrofit reduces annual emissions but makes the building dependent on a single electrically powered system with no contingency plan. What should be reviewed?",
 ["Only the annual carbon calculation", "Whether the emissions benefit creates unacceptable single points of failure and how critical service is maintained", "Only the equipment warranty font", "Whether the building can eliminate all alarms"], 1,
 "Decarbonization choices should be assessed alongside reliability, dependencies, critical loads, and contingency measures."),
("1.1 Climate drivers", "Which is the strongest evidence that a climate adaptation measure is working?",
 ["It was installed within budget", "Performance indicators show reduced exposure or consequences during relevant conditions and drills or tests validate readiness", "It appears in a sustainability brochure", "No one has inspected it since installation"], 1,
 "Implementation is not the same as effectiveness; monitoring, testing, and outcomes matter."),
("1.1 Climate drivers", "A facility faces wildfire smoke and heat simultaneously. Why is a combined scenario valuable?",
 ["Hazards always occur independently", "Interactions may constrain ventilation, filtration, cooling, and power at the same time", "It eliminates the need for an emergency plan", "It is relevant only to outdoor landscaping"], 1,
 "Compound events can create demands that are missed when hazards are assessed one at a time."),
("1.1 Climate drivers", "What should an owner do when climate data are too coarse to resolve site-specific flood exposure?",
 ["Treat the whole region as equally safe", "Use screening data as a starting point, then obtain appropriate local assessment and engineering input", "Ignore the hazard because exact data are unavailable", "Assume the lowest-risk map category is correct"], 1,
 "Regional screening identifies issues; site-specific decisions may need detailed topographic, drainage, and engineering assessment."),
("1.1 Climate drivers", "Which option is most likely to create maladaptation?",
 ["A shading strategy checked for daylight and wind effects", "A flood defence that shifts water toward neighbouring properties without considering wider impacts", "A risk assessment updated as conditions change", "A backup plan for critical loads"], 1,
 "Maladaptation reduces risk for one party or location while increasing vulnerability elsewhere or creating new harms."),
("1.1 Climate drivers", "Why include maintenance staff and operators in resilience planning?",
 ["They have no role after design", "They understand actual operating constraints, failure history, controls, and emergency procedures", "Their involvement replaces engineering analysis", "They should be responsible for all capital approvals"], 1,
 "Operational knowledge helps ensure measures are practical, maintainable, and usable under stress."),
("1.1 Climate drivers", "A flood-prone building is planning a major renovation. Which approach is best?",
 ["Consider flood exposure only after construction", "Integrate flood risk, critical equipment placement, drainage, safe access, and recovery needs early in design", "Use the same design as an inland site without checking", "Focus only on interior finishes"], 1,
 "Early integration can avoid expensive redesign and reduce vulnerabilities in layout and systems."),

("1.1 Owner goals", "An owner states a goal of carbon neutrality but has not defined boundaries or a target year. What is the most useful next step?",
 ["Immediately buy offsets for an undefined footprint", "Define emissions scopes and boundaries, baseline year, target timeline, and a credible reduction pathway", "Count only the easiest electricity meter", "Treat every avoided emission as a direct reduction"], 1,
 "A usable goal needs a defined inventory, boundary, timeline, and reduction strategy before residual emissions are addressed."),
("1.1 Owner goals", "An owner wants both resilient operations and lower emissions. Which decision process best aligns these goals?",
 ["Optimise only for lowest first cost", "Set measurable carbon and resilience outcomes, identify trade-offs, and evaluate whole-life options", "Choose separate systems without coordination", "Assume every resilience measure lowers emissions automatically"], 1,
 "Explicit shared criteria make trade-offs visible and help identify measures that support both objectives."),
("1.1 Owner goals", "Which is the clearest measurable owner goal?",
 ["Make the building greener soon", "Reduce absolute operational greenhouse-gas emissions 50% from a defined baseline by 2035", "Improve sustainability where possible", "Install equipment that looks efficient"], 1,
 "The goal is specific, measurable, time-bound, and tied to a baseline and emissions metric."),
("1.1 Owner goals", "A portfolio owner has a corporate net-zero commitment. What must be clarified before translating it to one building?",
 ["Whether the building's area is measured in square metres", "How the corporate boundary, asset-level targets, energy procurement, and embodied versus operational emissions are treated", "Only the tenant's preferred paint colour", "Whether every building has identical occupancy"], 1,
 "Corporate commitments need consistent boundaries and a practical method for allocating targets and actions across assets."),
("1.1 Owner goals", "A building owner prioritises occupant safety during outages. Which target is most aligned with that goal?",
 ["Reduce annual energy cost regardless of consequences", "Define the critical functions, acceptable interruption duration, and required backup or recovery performance", "Eliminate all preventive maintenance", "Measure only the number of installed sensors"], 1,
 "Resilience goals should specify the service that must be maintained and the acceptable duration or level of disruption."),
("1.1 Owner goals", "Which approach is best when an owner has a net-zero goal and limited capital?",
 ["Spend the full budget on a visible technology regardless of savings", "Prioritise measures by carbon impact, cost, risk reduction, dependencies, and timing, while protecting essential safety needs", "Ignore operations and maintenance", "Delay low-cost operational improvements"], 1,
 "Portfolio and project prioritisation should consider carbon, cost, risk, dependencies, and non-negotiable safety requirements."),
("1.1 Owner goals", "Why should owners distinguish energy targets from carbon targets?",
 ["Energy and carbon are identical under all conditions", "Carbon depends on energy quantity and its emissions factors, including grid and fuel changes", "Carbon targets never include electricity", "Energy targets measure occupant satisfaction directly"], 1,
 "The same energy use can have different emissions depending on fuel, grid mix, and procurement choices."),
("1.1 Owner goals", "A landlord and tenants disagree on who pays for efficiency upgrades and who receives utility savings. What is this commonly called?",
 ["A split incentive", "A climate normal", "A commissioning sequence", "A flood return period"], 0,
 "Split incentives occur when the party paying for an improvement does not receive the main financial benefit."),
("1.1 Owner goals", "Which owner goal best captures both resilience and decarbonization performance?",
 ["Install heat pumps in every case, regardless of context", "Reduce emissions while meeting defined thermal-safety and critical-service requirements under specified stress conditions", "Lower the utility bill for one month only", "Purchase a certification without operational targets"], 1,
 "Integrated goals pair carbon outcomes with explicit service, safety, and performance requirements."),
("1.1 Owner goals", "A sustainability target is being communicated to occupants. What makes it more credible?",
 ["Use ambitious language without a baseline", "Publish scope, baseline, milestones, actions, accountability, and progress reporting", "Report only positive results", "Avoid stating how emissions are measured"], 1,
 "Transparency about methodology, milestones, responsibilities, and progress improves credibility and accountability."),

("1.1 Risk mitigation", "A risk register rates extreme heat as high risk because it affects critical equipment and vulnerable occupants. What should follow?",
 ["Close the register and take no action", "Assign owners, select controls, set deadlines, and define indicators for residual risk", "Replace the risk rating with a marketing statement", "Transfer every risk to occupants"], 1,
 "Risk assessment should lead to accountable treatment actions and follow-up on residual risk."),
("1.1 Risk mitigation", "Which sequence most closely follows sound risk management?",
 ["Identify hazards, assess exposure and vulnerability, evaluate consequences, select controls, monitor residual risk", "Buy equipment, then decide what hazard it addresses", "Choose a solution before defining the problem", "Assess only the cost of the most recent incident"], 0,
 "A structured sequence links the hazard and consequences to appropriate treatment and ongoing review."),
("1.1 Risk mitigation", "A facility can reduce flood exposure by relocating vulnerable electrical equipment above expected flood levels. This is primarily an example of:",
 ["Reducing vulnerability through design", "Increasing exposure", "Carbon offsetting", "Occupant engagement only"], 0,
 "Moving critical equipment away from likely floodwater reduces its vulnerability to the hazard."),
("1.1 Risk mitigation", "A backup generator improves outage capability but adds combustion emissions and requires fuel deliveries that may be disrupted. What is the best evaluation?",
 ["Ignore emissions because resilience always overrides every other factor", "Assess critical-load needs, alternatives, runtime, fuel supply, emissions, testing, and safe operation", "Run the generator continuously to prove reliability", "Assume fuel deliveries cannot fail"], 1,
 "Backup options involve reliability, emissions, fuel logistics, maintenance, and safety trade-offs that need explicit assessment."),
("1.1 Risk mitigation", "Which is an example of risk transfer rather than risk reduction?",
 ["Elevating switchgear", "Purchasing insurance for defined flood losses", "Adding flood detection and alarms", "Improving drainage capacity"], 1,
 "Insurance transfers some financial consequences, but it does not remove the physical hazard or ensure continuity."),
("1.1 Risk mitigation", "A proposed adaptation project reduces a rare hazard but creates a serious daily indoor-air-quality risk. What should the owner do?",
 ["Approve it because the hazard is rare", "Compare all material benefits, risks, co-impacts, and alternatives before deciding", "Ignore occupant health in resilience work", "Evaluate only the installation price"], 1,
 "Risk controls should not introduce disproportionate health or safety harms; alternatives and co-impacts matter."),
("1.1 Risk mitigation", "Which measure is most likely to reduce the chance that a minor equipment failure becomes a major outage?",
 ["Remove alarms to simplify operations", "Use preventive maintenance, condition monitoring, spare-parts planning, and tested procedures", "Wait for all components to fail", "Keep no record of failures"], 1,
 "Maintenance and monitoring can detect degradation early and improve recovery readiness."),
("1.1 Risk mitigation", "Why should an owner identify interdependencies among power, water, communications, and HVAC?",
 ["A failure in one service can impair several building functions", "The systems never affect one another", "It makes risk analysis unnecessary", "It only matters for small residential buildings"], 0,
 "Critical systems depend on one another, so a single outage can cascade across services."),
("1.1 Risk mitigation", "A team is comparing adaptation options. Which approach best accounts for residual risk?",
 ["Assume the chosen measure makes the hazard impossible", "Estimate remaining risk after controls and decide whether it is acceptable or needs additional treatment", "Stop documenting risk after funding approval", "Use the same residual-risk rating for every option"], 1,
 "Controls rarely eliminate all risk; the remaining exposure and consequences must be reassessed."),
("1.1 Risk mitigation", "A building has a flood plan, but staff have never practised it. What is the main gap?",
 ["The plan is too well documented", "Operational readiness has not been validated through training, exercises, and review", "The building has no physical assets", "The plan automatically works because it exists"], 1,
 "Exercises test whether roles, communications, decisions, and procedures work under realistic conditions."),

("1.2 Resilience requirements", "An owner says a facility must remain resilient. What clarification is most important?",
 ["The preferred colour of emergency signage", "Which functions must continue, at what capacity, for how long, and under which hazards", "Whether resilience should be mentioned in a brochure", "Whether every space has the same criticality"], 1,
 "Resilience requirements need measurable service levels, timeframes, hazard assumptions, and critical functions."),
("1.2 Resilience requirements", "A laboratory requires stable temperature and humidity for valuable research. Which requirement should be specified?",
 ["A generic promise to install efficient HVAC", "Permitted environmental ranges, duration of excursions, monitoring, alarms, and recovery criteria", "Only the equipment brand", "Only the annual utility budget"], 1,
 "Critical environmental conditions should be expressed as measurable operating limits and response requirements."),
("1.2 Resilience requirements", "A tenant needs access during severe weather, but the site may lose public transport and road access. What should the resilience plan include?",
 ["Only internal HVAC controls", "Access routes, staffing contingencies, remote operations where feasible, communications, and essential deliveries", "A guarantee that roads will remain open", "No continuity measures because access is external"], 1,
 "Facility resilience depends on external infrastructure and people, not only on equipment inside the property."),
("1.2 Resilience requirements", "Which is the best basis for deciding whether to add redundant cooling equipment?",
 ["Install redundancy in every system regardless of cost or criticality", "Assess consequence of failure, required availability, maintainability, recovery time, and whole-life cost", "Use only the vendor's largest model", "Base the decision on equipment colour"], 1,
 "Redundancy should be justified by service criticality, failure consequences, maintenance needs, and cost."),
("1.2 Resilience requirements", "A facility's emergency power can run lights but not the controls needed to operate the cooling plant. What does this reveal?",
 ["A complete resilience solution", "A dependency mismatch between backed-up loads and the systems required to deliver the critical service", "That cooling never needs power", "That emergency power should be removed"], 1,
 "Backup plans must include the full chain of equipment and controls needed for the critical function."),
("1.2 Resilience requirements", "How should resilience requirements for a multi-tenant office be established?",
 ["Assume all tenants have identical needs", "Engage the owner, facility team, tenants, and critical service providers to agree service priorities and responsibilities", "Let the equipment supplier decide alone", "Exclude tenants from communication"], 1,
 "Different occupants may have different critical needs; clear consultation and roles help create workable requirements."),
("1.2 Resilience requirements", "A resilience standard requires testing of emergency systems. Which evidence is strongest?",
 ["A purchase order only", "Documented tests under defined conditions, recorded results, corrective actions, and retesting", "A verbal statement that equipment is new", "A photograph of the equipment"], 1,
 "Testing evidence demonstrates actual performance and tracks unresolved defects."),
("1.2 Resilience requirements", "Which requirement is most useful for a building that supports emergency response operations?",
 ["Maximum acceptable downtime for critical functions and a verified continuity plan", "A target for decorative lighting only", "A promise to review risk in ten years", "A requirement that all rooms be identical"], 0,
 "Critical facilities need explicit availability and recovery criteria tied to their mission."),
("1.2 Resilience requirements", "A facility is vulnerable to power outages during extreme weather. What should a continuity analysis consider beyond generator capacity?",
 ["Fuel availability, transfer equipment, maintenance, staffing, critical-load sequencing, and outage duration", "Only the generator's paint finish", "Only average monthly electricity use", "Only the number of parking spaces"], 0,
 "Generator capacity alone does not guarantee usable backup; dependencies and operating arrangements matter."),
("1.2 Resilience requirements", "Why should resilience requirements be reviewed after major occupancy or equipment changes?",
 ["The change may alter loads, critical functions, and system dependencies", "Requirements should never change", "Only the building's appearance changes", "It eliminates the need for commissioning"], 0,
 "Resilience requirements should reflect the building's current use, loads, people, and systems."),

("1.2 Occupant comfort and IEQ", "A building lowers outdoor-air ventilation to save energy, but occupant complaints and CO2 readings rise. What is the best response?",
 ["Keep reducing ventilation because energy is the only objective", "Verify ventilation and occupancy, investigate IAQ, and optimise energy recovery and controls without compromising health", "Disable sensors", "Assume CO2 is a direct measurement of every pollutant"], 1,
 "Energy savings should not compromise ventilation or health; diagnose conditions and use efficient ventilation strategies."),
("1.2 Occupant comfort and IEQ", "Which set of factors best represents indoor environmental quality?",
 ["Thermal comfort, ventilation, pollutants, lighting, acoustics, and moisture", "Only annual energy cost", "Only exterior appearance", "Only the number of thermostats"], 0,
 "IEQ covers multiple indoor conditions affecting health, comfort, and performance."),
("1.2 Occupant comfort and IEQ", "A retrofit improves airtightness but does not review ventilation. What risk could arise?",
 ["Indoor pollutants and moisture may accumulate if ventilation is inadequate", "Airtightness always eliminates pollutants", "Indoor humidity becomes irrelevant", "Heating and cooling systems no longer need controls"], 0,
 "A tighter envelope can reduce uncontrolled leakage, so designed and properly operated ventilation becomes important."),
("1.2 Occupant comfort and IEQ", "Occupants in perimeter zones complain of glare and overheating. Which intervention best addresses both?",
 ["Increase lighting levels and remove blinds", "Evaluate exterior shading, glazing, glare control, daylight, and zone-level controls", "Lower ventilation to zero", "Set all zones to the same temperature without investigation"], 1,
 "Shading and well-designed controls can reduce solar heat gains and glare while preserving useful daylight."),
("1.2 Occupant comfort and IEQ", "Why should a decarbonization project evaluate combustion appliances in occupied spaces?",
 ["Combustion can create indoor pollutants and safety risks, depending on appliance and ventilation conditions", "Combustion appliances always improve indoor air quality", "Combustion has no connection to occupant safety", "Only outdoor pollutants matter indoors"], 0,
 "Combustion equipment can introduce pollutants and requires appropriate venting, maintenance, and safety controls."),
("1.2 Occupant comfort and IEQ", "A building is using demand-controlled ventilation. Which safeguard is essential?",
 ["Trust one sensor forever without calibration", "Ensure sensors, control sequences, minimum ventilation, and occupancy assumptions are verified", "Allow ventilation to fall to zero under every condition", "Disable alarms whenever a sensor disagrees"], 1,
 "Demand control depends on reliable sensing and sequences that maintain required ventilation and safe conditions."),
("1.2 Occupant comfort and IEQ", "A heatwave causes indoor temperatures to exceed safe limits for some occupants. Which response is most appropriate?",
 ["Treat all occupants as equally heat tolerant", "Use a heat-response plan with monitoring, vulnerable-occupant considerations, cooling priorities, and communications", "Wait for complaints before checking conditions", "Prioritise energy savings over safety"], 1,
 "Heat response should prioritise health and safety, account for differing vulnerabilities, and define triggers and actions."),
("1.2 Occupant comfort and IEQ", "A low-carbon material is proposed for interior use, but its emissions data are incomplete. What should the project team do?",
 ["Assume low carbon means harmless indoors", "Review relevant product emissions and health evidence, and specify appropriate testing or documentation", "Ignore occupant exposure", "Approve it based only on colour"], 1,
 "Embodied-carbon benefits do not automatically establish low chemical emissions or suitability for indoor use."),
("1.2 Occupant comfort and IEQ", "Which method gives the most useful picture of occupant comfort after a retrofit?",
 ["Energy bills alone", "Combine measured conditions, system data, and occupant feedback across relevant seasons and zones", "A single tour of the lobby", "The contractor's completion date"], 1,
 "Comfort evaluation benefits from objective measurements and feedback over time and across spaces."),
("1.2 Occupant comfort and IEQ", "Why can poor acoustics matter in a high-performance building?",
 ["Acoustic conditions affect comfort, concentration, and occupant experience", "Acoustics determine the grid emissions factor", "Acoustics are unrelated to indoor environment", "Poor acoustics always lower energy use"], 0,
 "IEQ includes acoustic comfort as well as air, thermal, visual, and moisture conditions."),

("1.2 Asset value", "Which factor most directly supports the long-term value of a decarbonized building?",
 ["Verified performance, manageable operating costs, compliance readiness, and occupant demand", "A sustainability claim with no data", "Higher energy use with no explanation", "Avoiding all maintenance records"], 0,
 "Market value can be supported by credible performance, lower operating risk, regulatory readiness, and tenant appeal."),
("1.2 Asset value", "What is a potential stranded-asset risk for a carbon-intensive building?",
 ["It may face higher retrofit costs, reduced demand, or lower value as market and policy expectations change", "It is guaranteed to appreciate", "It will never need maintenance", "It is automatically exempt from regulation"], 0,
 "Changing policy, technology, financing, and tenant expectations can reduce the competitiveness of high-carbon assets."),
("1.2 Asset value", "A landlord wants to claim that an energy retrofit increased asset value. Which evidence is most persuasive?",
 ["A marketing slogan", "Measured energy and emissions performance, cost data, tenant outcomes, and relevant market evidence", "A list of unverified intentions", "Only the equipment's purchase price"], 1,
 "Credible value claims need measured outcomes and evidence connecting performance to costs, tenant demand, or market conditions."),
("1.2 Asset value", "Why can building commissioning and ongoing performance verification protect asset value?",
 ["They help ensure systems operate as intended and identify performance drift", "They guarantee every tenant will renew", "They eliminate every future capital expense", "They are unrelated to system performance"], 0,
 "Commissioning and monitoring help avoid persistent underperformance, comfort problems, and unnecessary operating costs."),
("1.2 Asset value", "Which approach best evaluates a proposed efficiency investment from an owner's perspective?",
 ["Compare first cost only", "Consider capital cost, operating savings, maintenance, replacement, risk, incentives, and useful life", "Ignore equipment life", "Assume utility rates never change"], 1,
 "Whole-life analysis considers both initial and ongoing costs and relevant risks across the asset's life."),
("1.2 Asset value", "A building has a high energy-performance rating but frequent tenant complaints. What is the best conclusion?",
 ["The rating proves that the building is high quality in every respect", "Asset performance should include comfort, service quality, actual operation, and tenant experience as well as energy", "Tenant experience is irrelevant to value", "The complaints should be excluded from all analysis"], 1,
 "Energy metrics alone do not capture all factors influencing usability, reputation, retention, and value."),
("1.2 Asset value", "How can transparent carbon and energy data help a property owner?",
 ["Support investment decisions, reporting, tenant engagement, and credible comparison over time", "Guarantee a fixed sale price", "Replace all engineering assessments", "Remove the need for data quality checks"], 0,
 "Reliable data support decisions and communication, but do not by themselves guarantee a market outcome."),
("1.2 Asset value", "A retrofit has a short simple payback but creates major maintenance complexity. What should the owner do?",
 ["Approve solely on simple payback", "Evaluate whole-life cost, maintainability, staff capability, reliability, and performance risk", "Ignore maintenance because the payback is short", "Assume complex systems never fail"], 1,
 "Simple payback omits important long-term costs and operational risks."),
("1.2 Asset value", "Which is the strongest reason to assess embodied carbon during a major renovation?",
 ["Materials and construction can represent significant emissions, and design choices affect the building's whole-life footprint", "Embodied carbon is always zero for existing buildings", "Operational energy is the only possible source of emissions", "Embodied carbon is identical to indoor CO2 concentration"], 0,
 "Whole-life carbon considers emissions from materials and construction as well as building operation and end of life."),
("1.2 Asset value", "A lender asks for credible building emissions information. What is the most appropriate response?",
 ["Provide estimates without stating assumptions", "Provide documented boundaries, data sources, calculation methods, assumptions, and relevant verification", "Send only a photograph of the plant room", "Report only whichever meter looks best"], 1,
 "Transparent methods and traceable data make carbon information more useful to lenders and other stakeholders."),

("1.2 Regulations and standards", "A project team identifies a new building decarbonization regulation. What should it do first?",
 ["Assume every requirement applies identically to every building", "Confirm jurisdiction, effective dates, building coverage, thresholds, compliance pathway, and responsible party", "Wait until the compliance deadline passes", "Treat a voluntary guideline as automatically law"], 1,
 "Applicability depends on jurisdiction, building type, thresholds, dates, and the regulation's specific requirements."),
("1.2 Regulations and standards", "Which distinction between a regulation and a voluntary standard is most accurate?",
 ["A regulation may be legally enforceable; a voluntary standard is generally adopted unless made mandatory through law or contract", "A voluntary standard is always a criminal law", "Regulations never have compliance deadlines", "Standards cannot inform design"], 0,
 "Legal status depends on the instrument and jurisdiction; standards can become mandatory when incorporated into rules or contracts."),
("1.2 Regulations and standards", "A building meets the energy code in force when it was built, but a new performance rule now applies to existing buildings. What should the owner conclude?",
 ["Original compliance necessarily exempts it forever", "Check the new rule's applicability and transition provisions; existing buildings may have new obligations", "Only new buildings can ever be regulated", "The rule can be ignored until equipment fails"], 1,
 "Some rules apply to existing buildings, with specific scope, timelines, exemptions, and compliance routes."),
("1.2 Regulations and standards", "A certification framework awards points for energy efficiency, but the owner must also meet mandatory emissions limits. What is the correct approach?",
 ["Use certification points as a substitute for legal compliance", "Treat certification and legal compliance as separate checks, meeting mandatory requirements first", "Ignore emissions limits if the building is certified", "Assume all certification systems have the same legal status"], 1,
 "Voluntary ratings and mandatory requirements serve different purposes; certification does not automatically establish compliance."),
("1.2 Regulations and standards", "Why should a design team maintain a compliance register?",
 ["To track applicable obligations, evidence, owners, deadlines, and status", "To replace all drawings", "To ensure no one reviews legal updates", "To list only voluntary aspirations"], 0,
 "A register creates accountability and traceability for compliance tasks and documentation."),
("1.2 Regulations and standards", "A standard is referenced by a contract but is not directly mandated by local law. How should the project treat it?",
 ["Ignore it because it is not a law", "Check the contractual obligation and apply the agreed requirements within the contract's scope", "Assume it overrides every law", "Treat it as optional regardless of contract wording"], 1,
 "Contractual requirements can be binding between parties even when the standard is not itself a statute."),
("1.2 Regulations and standards", "A building reports energy use but not the emissions factor or method used to convert energy into carbon. What is the problem?",
 ["The reported carbon result may not be reproducible or comparable", "The building must have zero emissions", "Energy data cannot ever be used for carbon calculations", "It automatically violates every standard"], 0,
 "Transparent emissions factors and methods are necessary to understand and compare reported carbon results."),
("1.2 Regulations and standards", "A new code requires improved envelope performance. What is a sensible design response?",
 ["Check the code's specific requirements and coordinate envelope, HVAC sizing, moisture, and commissioning", "Increase HVAC capacity without checking the envelope", "Assume insulation solves every indoor-air-quality issue", "Ignore thermal bridges and moisture risks"], 0,
 "Envelope and mechanical systems interact; compliance should be coordinated with comfort, moisture control, and system sizing."),
("1.2 Regulations and standards", "An owner operates buildings in several jurisdictions. What is the main compliance challenge?",
 ["Requirements, thresholds, timelines, and reporting methods may differ by location", "All jurisdictions necessarily use identical rules", "One building's permit guarantees portfolio-wide compliance", "Only national laws can ever affect buildings"], 0,
 "Multi-jurisdiction portfolios need location-specific tracking and consistent internal governance."),
("1.2 Regulations and standards", "Which practice best reduces the risk of missing a regulatory change?",
 ["Assign responsibility for horizon scanning, review authoritative sources, document impacts, and update plans", "Rely on informal rumours", "Review regulations only after a fine", "Assume current rules will never change"], 0,
 "Defined responsibility and a repeatable review process help identify changes early enough to act."),

("1.2 Social impacts", "A building decarbonization retrofit is planned in a low-income housing complex. Which social consideration is most important?",
 ["Maximise disruption to prove the project is ambitious", "Protect affordability, health, accessibility, and continuity while engaging residents meaningfully", "Assume every resident has identical needs", "Evaluate carbon savings and ignore displacement risk"], 1,
 "A just transition considers who benefits, who bears costs, and how to protect residents and vulnerable groups."),
("1.2 Social impacts", "An energy retrofit requires temporary relocation of occupants. What is the most responsible planning approach?",
 ["Provide notice, accessible communication, suitable alternatives, support, and a clear return plan", "Inform residents only after work starts", "Assume relocation has no social impact", "Exclude residents from all decisions"], 0,
 "Early communication and practical support reduce disruption and help protect occupants' rights and wellbeing."),
("1.2 Social impacts", "A building upgrade lowers energy bills but uses controls that some occupants cannot easily operate. What should the owner do?",
 ["Keep the controls because energy savings are the only goal", "Use accessible, understandable controls and provide training in appropriate languages and formats", "Remove all user controls", "Assume every occupant has the same abilities"], 1,
 "Usability and accessibility help ensure that performance benefits are shared and occupants can operate the building safely."),
("1.2 Social impacts", "A retrofit creates local construction jobs. Which additional step helps maximise the social benefit?",
 ["Consider fair wages, safe working conditions, local hiring access, and skills development", "Avoid all worker training", "Measure only the number of installed devices", "Assume every job is automatically high quality"], 0,
 "Job creation is more beneficial when work is safe, fair, accessible, and supports lasting skills."),
("1.2 Social impacts", "A carbon-reduction plan increases rents after renovations, potentially displacing existing residents. What issue does this raise?",
 ["The distribution of costs and benefits and the risk of green gentrification or displacement", "Only the building's cooling efficiency", "A reason to stop measuring emissions", "Proof that every retrofit raises rents"], 0,
 "Decarbonization can create distributional impacts; affordability and displacement should be assessed and mitigated."),
("1.2 Social impacts", "Why is occupant engagement important before changing building schedules and temperature settings?",
 ["It reveals actual needs, operating patterns, health considerations, and likely acceptance barriers", "It guarantees that no technical analysis is needed", "It is useful only after the project closes", "It eliminates the need to explain changes"], 0,
 "Engagement can surface needs and practical barriers, improving both design decisions and adoption."),
("1.2 Social impacts", "A project team is selecting which buildings to retrofit first. Which equity-aware method is strongest?",
 ["Prioritise only the buildings with the wealthiest tenants", "Combine emissions potential with safety, vulnerability, energy burden, service criticality, and feasibility", "Choose buildings by exterior appearance", "Ignore who is affected by poor building performance"], 1,
 "A fair prioritisation process considers carbon impact alongside vulnerability, affordability, health, and feasibility."),
("1.2 Social impacts", "A building's electrification may reduce local combustion pollution but increase electricity demand. Which social question should be assessed?",
 ["Whether benefits and burdens are distributed fairly and whether grid reliability and affordability are protected", "Only whether the equipment is new", "Whether occupants can see the equipment", "Whether reporting can be avoided"], 0,
 "Social assessment should consider local air quality, energy affordability, grid impacts, and distribution of benefits."),
("1.2 Social impacts", "What is the best way to evaluate whether a decarbonization programme is socially successful?",
 ["Report only tonnes of CO2 saved", "Track carbon and energy outcomes alongside affordability, comfort, health, access, disruption, and stakeholder feedback", "Count only project meetings", "Assume there are no unintended impacts"], 1,
 "Social outcomes require their own indicators, not just carbon metrics."),
("1.2 Social impacts", "Residents distrust a retrofit programme because earlier projects were poorly communicated. What is the strongest response?",
 ["Issue a final announcement after decisions are irreversible", "Engage early, disclose trade-offs, respond to concerns, explain complaint routes, and report back on actions", "Avoid questions about costs", "Use technical jargon to discourage disagreement"], 1,
 "Trust is built through meaningful participation, transparency, accessible communication, and visible follow-through."),

("Integrated Domain 1", "A proposed heat-pump retrofit reduces direct emissions, but the site experiences outages during heatwaves. What is the best decision framework?",
 ["Reject electrification automatically", "Compare lifecycle emissions and efficiency while testing peak loads, backup strategy, critical services, and future climate conditions", "Approve based only on equipment efficiency", "Use annual energy cost as the sole criterion"], 1,
 "Integrated decisions consider decarbonization benefits together with reliability, critical services, and climate risk."),
("Integrated Domain 1", "An owner must choose between a low-cost measure with modest savings and a more expensive measure that reduces emissions and flood risk. What should guide the choice?",
 ["First cost alone", "Whole-life costs and benefits, carbon reduction, avoided risk, occupant impacts, and owner requirements", "The number of pages in the proposal", "A blanket rule that expensive options are always better"], 1,
 "A multi-criteria, whole-life assessment can account for benefits that a simple first-cost comparison misses."),
("Integrated Domain 1", "A building's emissions fall after grid electricity becomes cleaner, even though its electricity use is unchanged. What does this show?",
 ["Carbon performance can change due to emissions factors as well as energy demand", "Efficiency necessarily improved", "The energy meter is useless", "All direct fuel emissions must also have fallen"], 0,
 "Emissions depend on both consumption and the carbon intensity of the energy source."),
("Integrated Domain 1", "A portfolio dashboard shows excellent average energy intensity, but one critical site has repeated service failures. What is the best interpretation?",
 ["The portfolio average proves every site is resilient", "Portfolio averages can hide critical site-level risk; examine distribution, criticality, and individual performance", "The critical site should be removed from reporting", "Energy intensity directly measures every resilience outcome"], 1,
 "Aggregated metrics should be complemented by site-specific risk and critical-service measures."),
("Integrated Domain 1", "Which project brief most effectively translates Domain 1 drivers into design requirements?",
 ["Make the building sustainable and resilient", "Specify carbon baseline and targets, climate hazards, critical service levels, IEQ criteria, compliance obligations, asset objectives, and social safeguards", "Specify only a preferred technology", "Leave performance decisions until commissioning"], 1,
 "A useful brief turns broad drivers into measurable, coordinated requirements for design, operation, compliance, and people."),
]

# Add 50 more distinct questions using scenario-based application prompts and carefully keyed answers.
# These questions deepen the same listed competencies without requiring external libraries.
EXTRA_QUESTIONS = [
("1.1 Climate drivers", "A cooling plant's design basis uses a weather percentile that is no longer suitable for the owner's stated risk tolerance. What is the best action?", ["Retain it because it is familiar", "Revisit design conditions with climate projections, criticality, and acceptable service risk", "Choose the mildest available weather file", "Increase the setpoint and stop analysis"], 1, "Design conditions should reflect the asset's risk tolerance and credible future conditions."),
("1.1 Climate drivers", "A building's energy use rises during smoke episodes because filtration pressure drop increases. What should be considered?", ["Filter efficiency, fan energy, replacement frequency, indoor air targets, and operating procedures together", "Remove filtration whenever smoke is present", "Ignore fan energy and indoor air quality", "Disable filter monitoring"], 0, "Filtration choices affect health protection, pressure drop, fan energy, and maintenance."),
("1.1 Climate drivers", "Which finding most strongly suggests that a climate hazard assessment is too generic?", ["It identifies site-specific exposure and critical systems", "It lists hazards but does not connect them to building location, systems, occupants, or consequences", "It documents assumptions and data sources", "It includes a review date"], 1, "A useful assessment translates hazards into specific exposure, vulnerability, and consequences."),
("1.1 Climate drivers", "A site is exposed to sea-level rise and storm surge over the next several decades. Which asset-planning response is strongest?", ["Assess exposure over the asset life and compare protection, adaptation, relocation, and residual risk options", "Use only last year's tide observations", "Assume temporary barriers solve every future scenario", "Ignore access and utility connections"], 0, "Long-term coastal risk can affect the site, services, access, and value, so multiple strategies and residual risks matter."),
("1.1 Climate drivers", "A facility's cooling system is water-cooled. During drought, what should be examined first?", ["Water dependency, restrictions, alternative operating modes, and critical cooling needs", "Only the annual lighting schedule", "Whether the building can stop collecting data", "Only the number of chillers"], 0, "Water-cooled systems have a dependency that can become a critical constraint during drought."),
("1.1 Climate drivers", "Why is a climate vulnerability assessment different from a hazard list?", ["It connects hazards to exposure, sensitivity, adaptive capacity, and consequences", "It contains only weather statistics", "It replaces maintenance planning", "It assumes every building is equally exposed"], 0, "Vulnerability analysis explains how a particular asset may be affected, not merely which hazards exist."),
("1.1 Climate drivers", "A building's resilience plan relies on a nearby district cooling network. What should be verified?", ["Network outage scenarios, service-level commitments, recovery times, and contingency options", "Only the network operator's logo", "That off-site infrastructure cannot fail", "Only the building's annual lighting use"], 0, "External service dependencies need their own reliability assumptions and contingencies."),
("1.1 Climate drivers", "A design team wants to use future climate data but has several credible datasets. What is best practice?", ["Select whichever produces the lowest cost without disclosure", "Document sources and assumptions, compare sensitivities, and test robust design choices", "Average every dataset without checking relevance", "Ignore all projections"], 1, "Transparent comparison and sensitivity testing help manage differences between credible projections."),
("1.1 Climate drivers", "Which is the strongest example of a no-regret adaptation measure?", ["A measure with benefits under current conditions and across plausible future scenarios", "A measure that works only if one precise forecast occurs", "A measure that creates new health risks", "A measure with no identified hazard pathway"], 0, "No-regret measures provide value now and remain useful across a range of future conditions."),
("1.1 Climate drivers", "A heat event threatens occupants and may also reduce transformer capacity. What does this indicate?", ["Climate risk can affect both the building and the infrastructure it depends on", "Only indoor systems matter", "The utility network is always independent of weather", "Comfort targets eliminate grid risk"], 0, "Heat can affect building loads and the performance of external electricity infrastructure at the same time."),
("1.1 Owner goals", "An owner sets a carbon target but permits floor-area growth. Which metric pair is most informative?", ["Absolute emissions and an appropriate intensity metric", "Only the number of sustainability meetings", "Only the building's age", "Only renewable energy certificates purchased"], 0, "Absolute emissions show total impact while intensity can help interpret performance as the portfolio changes."),
("1.1 Owner goals", "A goal says 'net zero by 2040' but relies on large future offsets. What should be clarified?", ["Near-term gross reductions, residual emissions, boundary, quality of claims, and treatment of offsets", "Only the colour of the net-zero logo", "Whether the target can remain unmeasured", "How to avoid a baseline"], 0, "A credible pathway prioritises actual reductions and transparently addresses residual emissions and claims."),
("1.1 Owner goals", "A facility owner and operator have different sustainability priorities. What is the best governance response?", ["Leave priorities implicit", "Agree decision rights, performance targets, data responsibilities, and escalation routes", "Let each party use unrelated carbon boundaries", "Measure results only at contract end"], 1, "Clear governance aligns incentives and responsibilities across ownership and operation."),
("1.1 Owner goals", "Why might an owner set separate targets for operational and embodied carbon?", ["They arise from different sources and often require different levers, data, and timing", "They are always numerically identical", "Embodied carbon is part of indoor air concentration", "Separate targets prevent any comparison"], 0, "Operational and embodied emissions differ in source and reduction strategy, so separate tracking improves accountability."),
("1.1 Owner goals", "A resilience goal says the building should 'recover quickly'. How can it be improved?", ["Define recovery time objectives for critical functions and conditions that trigger them", "Remove all time references", "Use a larger font", "Replace the goal with a carbon offset target"], 0, "Recovery objectives make resilience testable and support clear design and operational decisions."),
("1.1 Risk mitigation", "A risk control depends on staff manually closing flood gates, but staff may not reach the site during a storm. What is the key weakness?", ["The control depends on a potentially unavailable action at the moment of hazard", "Manual systems are always better", "Flood gates remove all exposure", "Staff availability is not a resilience issue"], 0, "Controls should be feasible under the conditions in which they are needed, with fail-safe or backup arrangements where appropriate."),
("1.1 Risk mitigation", "A risk assessment gives a high score to a low-likelihood event with catastrophic consequences. What should the team do?", ["Discard it because likelihood is low", "Evaluate the risk method, critical consequences, tolerability, and proportionate treatment", "Treat every risk score as exact science", "Only assess frequent minor events"], 1, "Low likelihood does not automatically make a catastrophic consequence acceptable; use the owner's risk criteria."),
("1.1 Risk mitigation", "A resilience measure shifts floodwater onto a neighbouring site. Which principle is most relevant?", ["Avoid transferring risk to others and evaluate wider system impacts", "Only assess the owner's property boundary", "Neighbouring impacts are never relevant", "Count the measure as successful without consultation"], 0, "Risk reduction should not create harmful external impacts or simply move vulnerability elsewhere."),
("1.1 Risk mitigation", "A building has a written emergency plan but outdated contact details and untested communications. What is needed?", ["Periodic review, contact validation, exercises, and corrective actions", "No change because a plan exists", "Delete the contact list", "Focus only on annual energy use"], 0, "Plans require upkeep and testing to remain usable when an incident occurs."),
("1.1 Risk mitigation", "How should a team compare a hard engineering defence with an operational warning procedure?", ["Compare risk reduction, reliability, lead time, failure modes, maintenance, and consequences", "Assume warnings are always sufficient", "Assume engineering measures never fail", "Compare only their visual appearance"], 0, "Different controls have different failure modes; layered strategies may be more reliable than one control."),
("1.2 Resilience requirements", "A building owner specifies 99.9% availability but no method of measurement. What is missing?", ["A defined service, measurement period, exclusions, evidence method, and accountability", "A more colourful dashboard", "A higher electricity bill", "A list of unrelated hazards"], 0, "Availability targets need an agreed definition and measurement method to be enforceable and meaningful."),
("1.2 Resilience requirements", "A critical facility shares a service entrance with a flood-prone loading area. What requirement should be considered?", ["Safe alternative access and continuity for essential deliveries and responders", "Only the entrance's appearance", "No contingency because the facility is critical", "A rule that deliveries stop permanently"], 0, "Access and logistics can be critical dependencies during an emergency."),
("1.2 Resilience requirements", "A resilience design proposes a battery system. Which requirements should be defined before sizing it?", ["Critical loads, required duration, recharge strategy, operating conditions, and safety constraints", "Only the battery's colour", "Only annual average energy use", "No end-of-life plan"], 0, "Battery sizing and value depend on the loads, duration, operating strategy, conditions, and safety."),
("1.2 Resilience requirements", "Why should emergency procedures identify who can authorise shutdown or evacuation?", ["Decisions under stress need clear authority and escalation", "It improves the building's energy rating automatically", "It removes the need for training", "It ensures hazards cannot occur"], 0, "Clear authority avoids delay and confusion during an incident."),
("1.2 Resilience requirements", "A building owner asks for resilience but rejects all maintenance funding. What is the likely issue?", ["Reliability measures may deteriorate without inspection, testing, and upkeep", "Maintenance has no relationship to resilience", "New equipment never needs servicing", "A written requirement guarantees performance"], 0, "Resilience is an ongoing capability, not only a capital installation."),
("1.2 Occupant comfort and IEQ", "A ventilation upgrade reduces energy use but creates drafts in occupied work areas. What should be done?", ["Evaluate air distribution, diffuser selection, control settings, and occupant conditions", "Assume drafts are necessary for efficiency", "Disable all ventilation", "Measure only outdoor temperature"], 0, "Comfort depends on air movement and distribution as well as ventilation quantity and energy use."),
("1.2 Occupant comfort and IEQ", "A building reports low average CO2 but has complaints about odours and irritation. What is the soundest interpretation?", ["CO2 alone does not measure every indoor pollutant or comfort issue", "Low CO2 proves every aspect of IAQ is excellent", "Odours are always imaginary", "The solution is always to close windows"], 0, "IAQ evaluation may require source investigation and pollutant-specific measures beyond CO2."),
("1.2 Occupant comfort and IEQ", "A retrofit changes lighting to reduce electricity use, but occupants report visual discomfort. What should be reviewed?", ["Illuminance, glare, colour rendering, daylight, task needs, and controls", "Only the carbon factor of gas", "Only the boiler efficiency", "Whether occupants can be ignored"], 0, "Visual comfort includes several factors and should be evaluated with actual task and occupant needs."),
("1.2 Occupant comfort and IEQ", "A building has persistent condensation after an envelope retrofit. Which investigation is most appropriate?", ["Review thermal bridges, vapour and air movement, surface temperatures, humidity, and ventilation", "Add fragrance to conceal odours", "Ignore the issue if energy use fell", "Close all outdoor-air paths without assessment"], 0, "Condensation depends on moisture sources, surface temperatures, air leakage, and ventilation conditions."),
("1.2 Occupant comfort and IEQ", "Why should commissioning include control sequences and sensors, not only equipment startup?", ["Incorrect sequences or sensor readings can undermine comfort, IAQ, and energy performance", "Sensors never affect operations", "Startup proves all future performance", "Control logic is unrelated to energy"], 0, "Systems must operate together as intended; faulty sensing or sequences can cause persistent problems."),
("1.2 Asset value", "A building's retrofit relies on proprietary controls that only one vendor can service. What asset concern should be considered?", ["Vendor dependency, maintainability, replacement cost, and continuity of service", "The controls' colour", "Whether the building has windows", "The fact that proprietary systems never fail"], 0, "Maintainability and vendor lock-in can affect lifecycle costs and operational risk."),
("1.2 Asset value", "Which statement about green certification and asset value is most defensible?", ["Certification guarantees a premium in every market", "Certification may support marketability, but value depends on local demand, verified performance, cost, and other asset attributes", "Certification eliminates the need for maintenance", "All certificates measure identical outcomes"], 1, "Certification can be useful evidence, but it does not guarantee a particular financial outcome."),
("1.2 Asset value", "An owner is deciding whether to replace functioning equipment early for carbon reasons. What analysis is needed?", ["Compare lifecycle emissions and costs, remaining useful life, refrigerants, energy savings, and disposal impacts", "Replace it immediately without calculation", "Consider only the new unit's rated efficiency", "Ignore embodied emissions"], 0,
 "Early replacement should consider operational savings against new equipment emissions, remaining life, and end-of-life impacts."),
("1.2 Asset value", "A building's energy data are incomplete and inconsistent. How does that affect investment decisions?", ["It increases uncertainty in baselines, savings estimates, and performance verification", "It guarantees larger savings", "It has no effect on confidence", "It proves the building is net zero"], 0,
 "Good data are essential for defensible baselines, business cases, and measurement of results."),
("1.2 Regulations and standards", "A code references a standard by a particular edition. What should the team verify?", ["Which edition and provisions are incorporated, plus any local amendments", "That every later edition automatically applies", "That standards never change", "Only the standard's cover design"], 0,
 "The legally applicable edition and amendments matter; newer editions are not automatically substituted."),
("1.2 Regulations and standards", "A project meets the minimum code but the owner has a more ambitious contractual carbon target. What should the team do?", ["Design to the applicable legal minimum and separately demonstrate how the contractual target will be met", "Assume code compliance proves the carbon target", "Ignore the target because it is more ambitious", "Use different baselines without disclosure"], 0,
 "Legal compliance and owner commitments can coexist and must be tracked as separate requirements."),
("1.2 Regulations and standards", "Why should a building owner retain evidence of compliance decisions and calculations?", ["It supports audits, accountability, future operations, and proof of the basis for decisions", "It makes future changes impossible", "It replaces all inspections", "It guarantees that regulations will not change"], 0,
 "Traceable evidence supports verification and helps future teams understand the assumptions and obligations."),
("1.2 Regulations and standards", "A standard is updated during design. What is the best response?", ["Check contract and regulatory applicability, assess impacts, and document whether the project must or should adopt the update", "Automatically ignore it", "Automatically redesign everything without checking scope", "Delete the previous design records"], 0,
 "The response depends on applicability and commitments, and should be assessed and documented rather than assumed."),
("1.2 Social impacts", "A retrofit is scheduled during exams at a school. Which planning response best reflects social impact awareness?", ["Coordinate noisy or disruptive work with school operations and protect safety and indoor conditions", "Ignore the school calendar", "Prioritise contractor convenience alone", "Disable all ventilation to keep dust out"], 0,
 "Timing, safety, noise, air quality, and continuity of learning are relevant impacts on occupants."),
("1.2 Social impacts", "A building has older occupants who may be more vulnerable to extreme heat. What is a fair planning approach?", ["Use universal assumptions and avoid consultation", "Assess differing needs, provide clear warnings and safe cooling options, and plan support without stigma", "Prioritise only the most vocal occupants", "Remove temperature monitoring"], 1,
 "Equitable resilience accounts for differing vulnerabilities and makes protective measures accessible."),
("1.2 Social impacts", "A project reduces emissions but increases energy bills for tenants because of a new tariff arrangement. What should be assessed?", ["Who bears costs and receives benefits, and whether affordability safeguards or contract changes are needed", "Only the project's carbon calculation", "Whether the equipment looks modern", "Whether tenant bills can be excluded from all evaluation"], 0,
 "Social performance includes affordability and the distribution of costs, not just building-level emissions."),
("1.2 Social impacts", "A consultation receives feedback mainly from people who can attend daytime meetings. What is the main limitation?", ["The feedback may not represent people facing time, access, language, or disability barriers", "Daytime attendees are always representative", "Consultation quality is unrelated to access", "The project should stop communicating"], 0,
 "Inclusive engagement uses accessible formats and varied channels so underrepresented groups can participate."),
("1.2 Social impacts", "Which indicator best complements carbon savings when evaluating a retrofit in affordable housing?", ["Change in household energy burden and reported thermal comfort", "Number of press releases", "Colour of the insulation", "Total number of contractor vehicles only"], 0,
 "Energy burden and comfort indicate whether residents experience practical benefits."),
("Integrated Domain 1", "A building has a net-zero target, an overheating risk, and a strict indoor-air-quality requirement. What is the strongest procurement approach?", ["Specify carbon, climate-performance, IEQ, commissioning, and verification requirements together", "Procure the lowest-priced HVAC unit only", "Use a generic sustainability label as the full specification", "Set no acceptance criteria"], 0,
 "Integrated procurement translates all major drivers into coordinated, verifiable performance requirements."),
("Integrated Domain 1", "A proposed measure saves energy but could worsen resilience during an outage. What should happen before approval?", ["Evaluate the trade-off, critical-service impact, and alternative designs or safeguards", "Approve it because any energy saving is beneficial", "Reject all energy measures permanently", "Ignore outage conditions"], 0,
 "Trade-offs should be evaluated explicitly and mitigated where they threaten required services."),
("Integrated Domain 1", "A facility has many sensors but no defined response to alarms. What is the main weakness?", ["Monitoring without decision rules, responsibility, and response procedures may not reduce risk", "More sensors always guarantee resilience", "Alarms are a substitute for maintenance", "Data cannot support building operations"], 0,
 "Data only create value when they inform defined actions and accountable responses."),
("Integrated Domain 1", "Which statement best describes a credible Domain 1 decarbonization plan?", ["It treats climate, owner goals, operations, asset value, compliance, and social impacts as separate unrelated issues", "It links climate hazards and emissions drivers to measurable requirements, prioritised actions, responsibilities, and verification", "It consists only of purchasing renewable energy", "It focuses only on the construction phase"], 1,
 "A credible plan connects drivers to requirements, actions, accountability, and evidence across the asset lifecycle."),
]

def build_question_bank():
    bank = list(RAW_QUESTIONS)
    bank.extend(EXTRA_QUESTIONS)
    # Make exactly 100 questions, preserving topic variety. The first 100 are all distinct.
    if len(bank) < 100:
        raise RuntimeError(f"Question bank has only {len(bank)} questions")
    return bank[:100]

class CDPQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CDP Exam Practice | Domain 1: Decarbonization Drivers")
        self.root.geometry("1000x760")
        self.root.minsize(820, 640)
        self.root.configure(bg="#f3f5f8")

        self.all_questions = build_question_bank()
        self.questions = []
        self.index = 0
        self.answers = {}        # question index -> selected option
        self.checked = set()     # questions answered/checked
        self.correct = set()
        self.review_mode = False
        self.review_indices = []

        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except tk.TclError:
            pass
        self.style.configure("TButton", font=("Segoe UI", 10), padding=8)
        self.style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=9)
        self.style.configure("TProgressbar", thickness=12)

        self.show_start_screen()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def heading(self, parent, title, subtitle=None):
        tk.Label(parent, text=title, font=("Segoe UI", 20, "bold"),
                 bg="#f3f5f8", fg="#172033").pack(anchor="w", pady=(0, 4))
        if subtitle:
            tk.Label(parent, text=subtitle, font=("Segoe UI", 10),
                     bg="#f3f5f8", fg="#596579", wraplength=900,
                     justify="left").pack(anchor="w", pady=(0, 14))

    def show_start_screen(self):
        self.clear()
        outer = tk.Frame(self.root, bg="#f3f5f8", padx=32, pady=28)
        outer.pack(fill="both", expand=True)
        self.heading(outer, "CDP Exam Practice Quiz",
                    "Domain 1: Decarbonization Drivers | 100 challenging multiple-choice questions")
        card = tk.Frame(outer, bg="white", padx=24, pady=22,
                        highlightbackground="#dce2eb", highlightthickness=1)
        card.pack(fill="x", pady=(12, 18))
        tk.Label(card, text="Topics covered", font=("Segoe UI", 13, "bold"),
                 bg="white", fg="#172033").pack(anchor="w", pady=(0, 10))
        topics = [
            "Climate-related drivers: building energy, climate hazards, resilience, owner goals, and risk mitigation",
            "Organization-related drivers: resilience requirements, occupant comfort and IEQ, health and safety",
            "Building asset value, regulations and standards, and the social impacts of reducing carbon",
        ]
        for topic in topics:
            tk.Label(card, text="• " + topic, font=("Segoe UI", 10), bg="white",
                     fg="#344054", wraplength=850, justify="left").pack(anchor="w", pady=4)

        tk.Label(outer, text="Quiz settings", font=("Segoe UI", 12, "bold"),
                 bg="#f3f5f8", fg="#172033").pack(anchor="w", pady=(0, 8))
        self.shuffle_var = tk.BooleanVar(value=True)
        self.instant_var = tk.BooleanVar(value=True)
        tk.Checkbutton(outer, text="Shuffle question order", variable=self.shuffle_var,
                       bg="#f3f5f8", activebackground="#f3f5f8", font=("Segoe UI", 10)).pack(anchor="w")
        tk.Checkbutton(outer, text="Show explanation immediately after checking an answer",
                       variable=self.instant_var, bg="#f3f5f8", activebackground="#f3f5f8",
                       font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 14))
        ttk.Button(outer, text="Start 100-question quiz", style="Primary.TButton",
                   command=self.start_quiz).pack(anchor="w")
        tk.Label(outer, text="Note: This is a practice aid based on the task list supplied, not an official CDP exam or official question bank.",
                 font=("Segoe UI", 9), bg="#f3f5f8", fg="#687386",
                 wraplength=900, justify="left").pack(anchor="w", pady=(18, 0))

    def start_quiz(self):
        self.questions = list(self.all_questions)
        if self.shuffle_var.get():
            random.shuffle(self.questions)
        self.index = 0
        self.answers.clear()
        self.checked.clear()
        self.correct.clear()
        self.review_mode = False
        self.review_indices = []
        self.show_question()

    def current_question(self):
        return self.questions[self.index]

    def show_question(self):
        self.clear()
        qdata = self.current_question()
        domain, question, options, answer, explanation = qdata
        outer = tk.Frame(self.root, bg="#f3f5f8", padx=24, pady=18)
        outer.pack(fill="both", expand=True)

        top = tk.Frame(outer, bg="#f3f5f8")
        top.pack(fill="x")
        tk.Label(top, text="CDP DOMAIN 1", font=("Segoe UI", 10, "bold"),
                 bg="#f3f5f8", fg="#52627a").pack(side="left")
        status_text = f"Question {self.index + 1} of {len(self.questions)}"
        tk.Label(top, text=status_text, font=("Segoe UI", 10, "bold"),
                 bg="#f3f5f8", fg="#172033").pack(side="right")

        progress = ttk.Progressbar(outer, maximum=len(self.questions),
                                   value=self.index + 1, mode="determinate")
        progress.pack(fill="x", pady=(10, 16))

        card = tk.Frame(outer, bg="white", padx=22, pady=20,
                        highlightbackground="#dce2eb", highlightthickness=1)
        card.pack(fill="both", expand=True)
        tk.Label(card, text=domain.upper(), font=("Segoe UI", 9, "bold"),
                 bg="white", fg="#3165a8").pack(anchor="w", pady=(0, 10))
        tk.Label(card, text=question, font=("Segoe UI", 13, "bold"),
                 bg="white", fg="#172033", wraplength=880, justify="left",
                 anchor="w").pack(fill="x", anchor="w", pady=(0, 18))

        self.selected_var = tk.IntVar(value=self.answers.get(self.index, -1))
        self.option_buttons = []
        for i, option in enumerate(options):
            rb = tk.Radiobutton(card, text=f"{chr(65+i)}.  {option}",
                                variable=self.selected_var, value=i,
                                font=("Segoe UI", 10), bg="white",
                                activebackground="white", fg="#273449",
                                selectcolor="#eaf1fb", wraplength=850,
                                justify="left", anchor="w", padx=8, pady=8,
                                command=self.save_selection)
            rb.pack(fill="x", anchor="w", pady=2)
            self.option_buttons.append(rb)

        self.feedback = tk.Frame(card, bg="white")
        self.feedback.pack(fill="x", pady=(14, 0))
        if self.index in self.checked:
            self.render_feedback()

        nav = tk.Frame(outer, bg="#f3f5f8")
        nav.pack(fill="x", pady=(14, 0))
        ttk.Button(nav, text="← Previous", command=self.previous_question,
                   state="normal" if self.index > 0 else "disabled").pack(side="left")
        ttk.Button(nav, text="Check answer", style="Primary.TButton",
                   command=self.check_answer).pack(side="left", padx=(8, 0))
        ttk.Button(nav, text="Next →", command=self.next_question,
                   state="normal" if self.index < len(self.questions)-1 else "disabled").pack(side="left", padx=(8, 0))
        ttk.Button(nav, text="Finish / Results", command=self.show_results).pack(side="right")
        ttk.Button(nav, text="Quit to menu", command=self.confirm_quit).pack(side="right", padx=(0, 8))

        score = len(self.correct)
        checked_count = len(self.checked)
        tk.Label(outer, text=f"Correct: {score}    |    Checked: {checked_count}/{len(self.questions)}",
                 font=("Segoe UI", 9), bg="#f3f5f8", fg="#596579").pack(anchor="w", pady=(10, 0))

    def save_selection(self):
        self.answers[self.index] = self.selected_var.get()
        # If the user changes an answer after checking, require re-checking it.
        if self.index in self.checked:
            self.checked.remove(self.index)
            self.correct.discard(self.index)
            for widget in self.feedback.winfo_children():
                widget.destroy()

    def check_answer(self):
        selected = self.selected_var.get()
        if selected < 0:
            messagebox.showinfo("Choose an option", "Select one of the four options before checking your answer.")
            return
        self.answers[self.index] = selected
        self.checked.add(self.index)
        correct_answer = self.current_question()[3]
        if selected == correct_answer:
            self.correct.add(self.index)
        else:
            self.correct.discard(self.index)
        self.render_feedback()

    def render_feedback(self):
        for widget in self.feedback.winfo_children():
            widget.destroy()
        domain, question, options, answer, explanation = self.current_question()
        selected = self.answers.get(self.index, -1)
        if self.index not in self.checked:
            return
        is_correct = selected == answer
        color = "#137547" if is_correct else "#b42318"
        label = "Correct!" if is_correct else "Not quite."
        tk.Label(self.feedback, text=label, font=("Segoe UI", 12, "bold"),
                 bg="white", fg=color).pack(anchor="w", pady=(0, 5))
        tk.Label(self.feedback, text=f"Correct answer: {chr(65+answer)}. {options[answer]}",
                 font=("Segoe UI", 10, "bold"), bg="white", fg="#172033",
                 wraplength=850, justify="left").pack(anchor="w", pady=(0, 5))
        if self.instant_var.get():
            tk.Label(self.feedback, text="Why: " + explanation, font=("Segoe UI", 10),
                     bg="white", fg="#344054", wraplength=850,
                     justify="left").pack(anchor="w")

    def previous_question(self):
        if self.index > 0:
            self.index -= 1
            self.show_question()

    def next_question(self):
        if self.index < len(self.questions) - 1:
            self.index += 1
            self.show_question()

    def confirm_quit(self):
        if messagebox.askyesno("Return to menu", "Return to the start screen? Current quiz answers will be cleared if you start again."):
            self.show_start_screen()

    def show_results(self):
        self.clear()
        total = len(self.questions)
        score = len(self.correct)
        checked_count = len(self.checked)
        percent = round(score / total * 100, 1) if total else 0
        outer = tk.Frame(self.root, bg="#f3f5f8", padx=28, pady=22)
        outer.pack(fill="both", expand=True)
        self.heading(outer, "Quiz results", "CDP Exam Practice | Domain 1: Decarbonization Drivers")

        card = tk.Frame(outer, bg="white", padx=22, pady=18,
                        highlightbackground="#dce2eb", highlightthickness=1)
        card.pack(fill="x", pady=(4, 16))
        tk.Label(card, text=f"{score} / {total}", font=("Segoe UI", 28, "bold"),
                 bg="white", fg="#172033").pack(anchor="w")
        tk.Label(card, text=f"{percent}% correct", font=("Segoe UI", 13, "bold"),
                 bg="white", fg="#3165a8").pack(anchor="w", pady=(2, 8))
        tk.Label(card, text=f"Answered and checked: {checked_count}/{total}",
                 font=("Segoe UI", 10), bg="white", fg="#596579").pack(anchor="w")
        tk.Label(card, text=f"Not yet checked: {total - checked_count}",
                 font=("Segoe UI", 10), bg="white", fg="#596579").pack(anchor="w")

        review = tk.LabelFrame(outer, text="Review answers", font=("Segoe UI", 11, "bold"),
                               bg="#f3f5f8", fg="#172033", padx=10, pady=10)
        review.pack(fill="both", expand=True)
        canvas = tk.Canvas(review, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(review, orient="vertical", command=canvas.yview)
        list_frame = tk.Frame(canvas, bg="white")
        list_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=list_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for i, item in enumerate(self.questions):
            domain, question, options, answer, explanation = item
            selected = self.answers.get(i, -1)
            checked = i in self.checked
            good = checked and selected == answer
            color = "#137547" if good else ("#b42318" if checked else "#7a8494")
            prefix = "Correct" if good else ("Incorrect" if checked else "Not checked")
            row = tk.Frame(list_frame, bg="white", padx=12, pady=10)
            row.pack(fill="x", anchor="w")
            tk.Label(row, text=f"{i+1}. [{prefix}] {domain}", font=("Segoe UI", 9, "bold"),
                     bg="white", fg=color, wraplength=850, justify="left").pack(anchor="w")
            tk.Label(row, text=question, font=("Segoe UI", 10, "bold"), bg="white",
                     fg="#172033", wraplength=850, justify="left").pack(anchor="w", pady=(3, 2))
            selected_text = "No answer selected" if selected < 0 else f"Your answer: {chr(65+selected)}. {options[selected]}"
            tk.Label(row, text=selected_text, font=("Segoe UI", 9), bg="white",
                     fg="#596579", wraplength=850, justify="left").pack(anchor="w")
            tk.Label(row, text=f"Correct answer: {chr(65+answer)}. {options[answer]}",
                     font=("Segoe UI", 9, "bold"), bg="white", fg="#172033",
                     wraplength=850, justify="left").pack(anchor="w", pady=(2, 0))
            tk.Label(row, text="Why: " + explanation, font=("Segoe UI", 9), bg="white",
                     fg="#344054", wraplength=850, justify="left").pack(anchor="w", pady=(2, 0))
            ttk.Separator(list_frame, orient="horizontal").pack(fill="x")

        buttons = tk.Frame(outer, bg="#f3f5f8")
        buttons.pack(fill="x", pady=(14, 0))
        ttk.Button(buttons, text="Retry all questions", style="Primary.TButton",
                   command=self.start_quiz).pack(side="left")
        ttk.Button(buttons, text="Return to menu", command=self.show_start_screen).pack(side="left", padx=8)
        ttk.Button(buttons, text="Close", command=self.root.destroy).pack(side="right")

def main():
    root = tk.Tk()
    app = CDPQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
