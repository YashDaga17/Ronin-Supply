# Requirements Document

## Introduction

Ronin Supply is a Python-based Retail Operating System that implements autonomous agents for supply chain management with hyper-local intelligence. The system consists of three integrated modules: The Merchant (agentic supply chain negotiator), The Seer (hyper-local micro-event forecaster), and The Salvager (visual grading & profit recovery engine). The system follows a modular monolith architecture with event-driven integration between modules, leveraging real-time web intelligence and advanced AI capabilities for maximum business value.

## Glossary

- **System**: The complete Ronin Supply retail operating system
- **The_Merchant**: AI-powered supply chain negotiation module
- **The_Seer**: Hyper-local demand forecasting module based on micro-events and real-world intelligence
- **The_Salvager**: Computer vision-based item grading and profit recovery engine
- **Scout_Agent**: Component that searches for supplier contact information using web intelligence
- **Negotiator_Agent**: Component that manages email negotiations with suppliers
- **Micro_Event**: Hyper-local events (concerts, weather, rallies) that impact specific geographic demand
- **Demand_Spike**: Predicted increase in product demand above baseline for specific locations/timeframes
- **Visual_Grading**: Computer vision analysis of returned item condition for profit recovery
- **Profit_Recovery**: Process of converting returned items into revenue through optimal resale channels
- **Resale_Channel**: Platform or method for selling graded returned items (eBay, Poshmark, refurb sites)
- **Event_Correlation**: Analysis linking past sales data with hyper-local real-world events
- **Auto_Personality**: Adaptive communication style feature for negotiations
- **Web_Intelligence**: Real-time web data extraction and analysis using Tavily API
- **Impact_Scoring**: PredictHQ's ML-ready scoring system for event demand impact

## Requirements

### Requirement 1: Supply Chain Negotiation

**User Story:** As a retail manager, I want an AI system to automatically negotiate with suppliers for the best prices, so that I can reduce procurement costs without manual intervention.

#### Acceptance Criteria

1. WHEN a negotiation is initiated, THE Scout_Agent SHALL search for supplier contact information using web scraping
2. WHEN supplier contacts are found, THE Negotiator_Agent SHALL draft personalized negotiation emails
3. WHEN drafting emails, THE Auto_Personality SHALL adapt communication style based on supplier characteristics
4. WHEN negotiations are ongoing, THE System SHALL track email threads and response patterns
5. WHEN a supplier responds, THE Negotiator_Agent SHALL analyze the response and generate appropriate follow-up emails
6. WHEN negotiations conclude, THE System SHALL record final pricing agreements in the supplier database

### Requirement 2: Hyper-Local Micro-Event Forecasting

**User Story:** As a inventory manager, I want to predict demand spikes from hyper-local micro-events with precise geographic and temporal accuracy, so that I can optimize inventory for specific locations and time windows.

#### Acceptance Criteria

1. WHEN The_Seer starts, THE System SHALL ingest data from PredictHQ, Tavily, OpenWeatherMap, and local event sources
2. WHEN micro-events are detected, THE System SHALL analyze impact scoring and geographic radius for demand correlation
3. WHEN correlating events with sales, THE System SHALL identify hyper-local patterns (zip code level) with temporal precision
4. WHEN demand spikes are predicted, THE System SHALL specify exact timeframes (48-hour windows) and confidence levels
5. WHEN high-impact events are identified, THE System SHALL trigger location-specific automatic ordering workflows
6. WHEN predictions are generated, THE System SHALL include geographic boundaries and expected demand multipliers

### Requirement 3: Visual Grading & Profit Recovery Engine

**User Story:** As a returns processor, I want an AI system to automatically grade returned items and route them to optimal resale channels for maximum profit recovery, so that I can convert losses into revenue.

#### Acceptance Criteria

1. WHEN a returned item photo is uploaded, THE Salvager SHALL analyze the image using Gemini 3 Flash Vision
2. WHEN analyzing photos, THE System SHALL detect defects, authenticity markers, completeness, and market condition
3. WHEN grading is complete, THE System SHALL assign profit recovery grades (Mint/Resell Full Price, Good/Discount, Parts/Refurb, Recycle)
4. WHEN items are graded, THE System SHALL automatically route them to optimal resale channels (eBay, Poshmark, Amazon Renewed, Parts)
5. WHEN routing decisions are made, THE System SHALL calculate expected profit recovery percentages and timeframes
6. WHEN resale listings are created, THE System SHALL generate optimized descriptions and pricing for each channel
7. WHEN fraud is suspected, THE System SHALL flag items for manual review with detailed analysis

### Requirement 4: Module Integration

**User Story:** As a system administrator, I want all three modules to work cohesively together, so that the system operates as a unified retail operating system.

#### Acceptance Criteria

1. WHEN The_Seer predicts a demand spike, THE System SHALL automatically trigger The_Merchant negotiation workflows
2. WHEN modules communicate, THE System SHALL use event-driven architecture for real-time responses
3. WHEN data is shared, THE System SHALL maintain consistency across product and supplier databases
4. WHEN operations occur, THE System SHALL log all inter-module communications for audit trails
5. WHEN conflicts arise between modules, THE System SHALL implement priority-based resolution mechanisms

### Requirement 5: Data Management

**User Story:** As a data analyst, I want all system data to be stored consistently and accessibly, so that I can analyze performance and generate reports.

#### Acceptance Criteria

1. WHEN data is stored, THE System SHALL use PostgreSQL with pgvector extension for all persistent data
2. WHEN storing orders and chats, THE System SHALL use Supabase as the primary storage backend
3. WHEN photos are uploaded, THE System SHALL store them with associated metadata in Supabase
4. WHEN vector embeddings are needed, THE System SHALL utilize pgvector for similarity searches
5. WHEN data integrity is required, THE System SHALL implement proper foreign key constraints and validation
6. WHEN backups are needed, THE System SHALL support automated database backup procedures

### Requirement 6: User Interface

**User Story:** As a retail operator, I want a unified dashboard to control all three systems, so that I can monitor and manage operations from a single interface.

#### Acceptance Criteria

1. WHEN the dashboard loads, THE System SHALL display real-time status of all three modules
2. WHEN viewing negotiations, THE System SHALL show active supplier conversations and their status
3. WHEN reviewing forecasts, THE System SHALL display predicted demand spikes with confidence levels
4. WHEN examining graded items, THE System SHALL show item photos, grades, and routing decisions
5. WHEN manual intervention is needed, THE System SHALL provide controls to override automated decisions
6. WHEN generating reports, THE System SHALL export data in common formats (CSV, PDF, Excel)

### Requirement 7: Advanced AI Engine Integration

**User Story:** As a system architect, I want cutting-edge AI capabilities across all modules, so that the system maintains superior intelligence and performance.

#### Acceptance Criteria

1. WHEN AI processing is required, THE System SHALL use Gemini 3 Flash as the primary AI engine for enhanced reasoning
2. WHEN agent orchestration is needed, THE System SHALL implement LangGraph for stateful workflow management
3. WHEN web intelligence is required, THE System SHALL use Tavily API for real-time web data extraction
4. WHEN natural language processing occurs, THE System SHALL maintain consistent prompt engineering patterns
5. WHEN AI responses are generated, THE System SHALL implement proper error handling and fallback mechanisms
6. WHEN API limits are approached, THE System SHALL implement intelligent rate limiting and priority queuing

### Requirement 8: Real-Time Web Intelligence Integration

**User Story:** As a data integration specialist, I want the system to leverage real-time web intelligence for superior market awareness, so that all decisions are based on current, comprehensive data.

#### Acceptance Criteria

1. WHEN connecting to PredictHQ API, THE System SHALL retrieve ML-ready event data with impact scoring for demand correlation
2. WHEN using Tavily API, THE System SHALL extract structured, AI-optimized web data for supplier research and market intelligence
3. WHEN accessing OpenWeatherMap, THE System SHALL fetch hyper-local weather data that impacts micro-regional demand
4. WHEN web scraping is needed, THE System SHALL use Tavily's optimized extraction with proper rate limiting
5. WHEN API failures occur, THE System SHALL implement intelligent retry mechanisms with exponential backoff
6. WHEN data freshness is critical, THE System SHALL refresh web intelligence sources according to event urgency

### Requirement 9: Email Communication

**User Story:** As a procurement manager, I want the system to handle email communications professionally and reliably, so that supplier relationships are maintained effectively.

#### Acceptance Criteria

1. WHEN sending emails, THE System SHALL use smtplib with proper authentication and security
2. WHEN composing messages, THE System SHALL generate professional, contextually appropriate content
3. WHEN tracking conversations, THE System SHALL parse email threads and maintain conversation history
4. WHEN emails fail to send, THE System SHALL retry with appropriate delays and log failures
5. WHEN receiving responses, THE System SHALL automatically parse and categorize supplier replies

### Requirement 10: Advanced Time-Series Analysis

**User Story:** As a demand planner, I want sophisticated forecasting capabilities with hyper-local precision, so that predictions are accurate and actionable for location-specific inventory decisions.

#### Acceptance Criteria

1. WHEN performing forecasting, THE System SHALL use Nixtla/StatsForecast for time-series analysis with geographic segmentation
2. WHEN correlating events with sales, THE System SHALL identify statistically significant patterns at zip code granularity
3. WHEN generating predictions, THE System SHALL provide confidence intervals and geographic impact boundaries
4. WHEN historical data is insufficient, THE System SHALL indicate low confidence and request more data
5. WHEN seasonal patterns exist, THE System SHALL incorporate seasonality into hyper-local forecasting models
6. WHEN anomalies are detected, THE System SHALL flag unusual patterns for manual review with geographic context

### Requirement 11: Profit Recovery Optimization

**User Story:** As a financial analyst, I want to maximize profit recovery from returned items, so that losses are minimized and revenue is optimized through intelligent resale strategies.

#### Acceptance Criteria

1. WHEN items are graded, THE System SHALL calculate expected profit recovery percentages for each resale channel
2. WHEN market conditions change, THE System SHALL dynamically adjust pricing strategies for optimal profit
3. WHEN resale channels are selected, THE System SHALL consider fees, audience, and time-to-sale factors
4. WHEN listings are created, THE System SHALL generate channel-optimized descriptions and competitive pricing
5. WHEN sales performance is tracked, THE System SHALL learn and improve routing decisions over time
6. WHEN profit thresholds are not met, THE System SHALL recommend alternative recovery strategies

### Requirement 12: Geographic Intelligence

**User Story:** As a regional manager, I want hyper-local intelligence for inventory decisions, so that each location is optimized for its specific market conditions and events.

#### Acceptance Criteria

1. WHEN events are analyzed, THE System SHALL determine precise geographic impact radius and intensity
2. WHEN demand is predicted, THE System SHALL specify exact zip codes and neighborhoods affected
3. WHEN inventory is allocated, THE System SHALL consider location-specific factors and constraints
4. WHEN events overlap geographically, THE System SHALL calculate cumulative demand impact
5. WHEN transportation costs are factored, THE System SHALL optimize inventory distribution across locations
6. WHEN local regulations apply, THE System SHALL incorporate compliance requirements into decisions