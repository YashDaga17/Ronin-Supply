# Implementation Plan: Ronin Supply

## Overview

This implementation plan converts the enhanced Ronin Supply design into discrete coding tasks that build incrementally toward a complete retail operating system. The system integrates three AI-powered modules (The Merchant, The Seer, The Salvager) with hyper-local intelligence, profit recovery optimization, and real-time web intelligence capabilities.

## Tasks

- [x] 1. Set up project infrastructure and core dependencies
  - Create Python project structure with FastAPI, PostgreSQL, and Supabase integration
  - Install and configure Gemini 3 Flash, Tavily API, PredictHQ, and other external services
  - Set up development environment with Docker containers for PostgreSQL and Redis
  - Configure environment variables and API keys for all external services
  - _Requirements: 5.1, 5.2, 7.1, 8.1, 8.2_

- [ ] 2. Implement core data models and database schema
  - [ ] 2.1 Create enhanced data models with geographic intelligence support
    - Implement Product, Supplier, GeographicEvent, HyperLocalForecast models
    - Create ProfitRecoveryItem, WebIntelligenceCache, EnhancedSupplier models
    - Add Pydantic validation and serialization for all models
    - _Requirements: 5.1, 12.1, 11.1_

  - [ ] 2.2 Write property test for data model validation
    - **Property 29: Exact Geographic Demand Specification**
    - **Validates: Requirements 12.2**

  - [ ] 2.3 Set up PostgreSQL with PostGIS and pgvector extensions
    - Create database schema with geographic tables and spatial indexes
    - Implement vector embeddings tables for supplier and product similarity
    - Set up proper foreign key constraints and data validation
    - _Requirements: 5.1, 5.4, 12.1_

  - [ ] 2.4 Write property test for database consistency
    - **Property 10: Database Consistency Maintenance** 
    - **Validates: Requirements 4.3**

- [ ] 3. Implement FastAPI server with WebSocket support
  - [ ] 3.1 Create FastAPI application with async support
    - Set up FastAPI server with CORS, authentication, and error handling
    - Implement WebSocket endpoints for real-time geographic intelligence updates
    - Create API routes for all three modules (Merchant, Seer, Salvager)
    - _Requirements: 6.1, 4.2_

  - [ ] 3.2 Implement authentication and security middleware
    - Set up JWT authentication for API access
    - Implement rate limiting and request validation
    - Add security headers and HTTPS configuration
    - _Requirements: 9.1, 7.5_

  - [ ] 3.3 Write unit tests for API endpoints
    - Test authentication, rate limiting, and error handling
    - Mock external API dependencies for consistent testing
    - _Requirements: 7.5, 9.1_

- [ ] 4. Checkpoint - Ensure infrastructure and API foundation works
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 5. Implement The Seer module (Hyper-Local Forecasting)
  - [ ] 5.1 Create PredictHQ integration for ML-ready event data
    - Implement PredictHQ API client with impact scoring retrieval
    - Create event data processing pipeline with geographic analysis
    - Set up automatic event monitoring and data refresh
    - _Requirements: 8.1, 2.1, 2.2_

  - [ ] 5.2 Write property test for PredictHQ data retrieval
    - **Property 16: PredictHQ ML-Ready Data Retrieval**
    - **Validates: Requirements 8.1**

  - [ ] 5.3 Implement Tavily API integration for web intelligence
    - Create Tavily API client for structured web data extraction
    - Implement intelligent caching with event-urgency based refresh
    - Set up rate limiting and error handling for web intelligence queries
    - _Requirements: 8.2, 7.3, 8.6_

  - [ ] 5.4 Write property test for web intelligence data extraction
    - **Property 17: Structured Web Data Extraction**
    - **Validates: Requirements 8.2**

  - [ ] 5.5 Create geographic intelligence system with PostGIS
    - Implement spatial queries for event impact radius calculation
    - Create zip code level demand analysis with geographic boundaries
    - Set up cumulative impact calculation for overlapping events
    - _Requirements: 12.1, 12.2, 12.4_

  - [ ] 5.6 Write property test for geographic impact analysis
    - **Property 28: Precise Geographic Impact Analysis**
    - **Validates: Requirements 12.1**

  - [ ] 5.7 Implement hyper-local forecasting engine with Nixtla StatsForecast
    - Set up StatsForecast with geographic segmentation capabilities
    - Create 48-hour precision forecasting with confidence intervals
    - Implement demand multiplier calculation based on event impact
    - _Requirements: 10.1, 2.4, 2.6_

  - [ ] 5.8 Write property test for temporal precision
    - **Property 3: Demand Spike Temporal Precision**
    - **Validates: Requirements 2.4**

- [ ] 6. Implement The Merchant module (Intelligent Negotiation)
  - [ ] 6.1 Create Scout Agent with Tavily web intelligence
    - Implement supplier research using Tavily API for comprehensive intelligence
    - Create supplier profile building with market reputation analysis
    - Set up contact information extraction and validation
    - _Requirements: 1.1, 8.2, 8.4_

  - [ ] 6.2 Write property test for Scout Agent web intelligence
    - **Property 12: Tavily Web Intelligence Integration**
    - **Validates: Requirements 7.3**

  - [ ] 6.3 Implement Negotiator Agent with Gemini 3 Flash
    - Create email composition with Auto-Personality adaptation
    - Implement cultural context analysis and communication style optimization
    - Set up negotiation tracking and conversation history management
    - _Requirements: 1.2, 1.3, 7.4_

  - [ ] 6.4 Write property test for communication adaptation
    - **Property 13: Consistent Prompt Engineering**
    - **Validates: Requirements 7.4**

  - [ ] 6.5 Create LangGraph workflow orchestration
    - Implement stateful workflows for Scout and Negotiator agent coordination
    - Set up event-driven triggers from Seer module for procurement
    - Create priority-based processing for urgent negotiations
    - _Requirements: 7.2, 4.1, 7.6_

  - [ ] 6.6 Write property test for workflow triggering
    - **Property 4: Location-Specific Workflow Triggering**
    - **Validates: Requirements 2.5**

- [ ] 7. Implement The Salvager module (Profit Recovery Engine)
  - [ ] 7.1 Create advanced visual grading pipeline with Gemini 3 Flash Vision
    - Implement image analysis for defect detection and authenticity verification
    - Create profit recovery grading system (Mint, Good, Parts, Recycle)
    - Set up fraud detection and manual review flagging
    - _Requirements: 3.1, 3.2, 3.3, 3.7_

  - [ ] 7.2 Write property test for visual analysis completeness
    - **Property 6: Enhanced Visual Analysis Completeness**
    - **Validates: Requirements 3.1, 3.2**

  - [ ] 7.3 Implement marketplace integration and automation
    - Create eBay, Poshmark, Amazon Renewed API integrations
    - Implement automated listing creation with channel-optimized descriptions
    - Set up dynamic pricing based on market conditions and competitive analysis
    - _Requirements: 3.4, 3.6, 11.2, 11.4_

  - [ ] 7.4 Write property test for channel optimization
    - **Property 10: Channel-Optimized Listing Generation**
    - **Validates: Requirements 3.6**

  - [ ] 7.5 Create profit recovery optimization engine
    - Implement multi-channel profit calculation and comparison
    - Create routing decision logic with fees, audience, and time-to-sale factors
    - Set up performance tracking and learning for routing improvement
    - _Requirements: 11.1, 11.3, 11.5_

  - [ ] 7.6 Write property test for profit optimization
    - **Property 22: Multi-Channel Profit Recovery Calculation**
    - **Validates: Requirements 11.1**

- [ ] 8. Checkpoint - Ensure all three modules work independently
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 9. Implement inter-module communication and event system
  - [ ] 9.1 Create event-driven architecture with PostgreSQL queues
    - Implement event publishing and subscription system
    - Set up dead letter queues for failed event processing
    - Create audit logging for all inter-module communications
    - _Requirements: 4.2, 4.4_

  - [ ] 9.2 Write property test for event communication
    - **Property 9: Inter-Module Event Communication** 
    - **Validates: Requirements 4.2, 4.4**

  - [ ] 9.3 Implement cross-module data consistency mechanisms
    - Create transaction boundaries for multi-module operations
    - Set up data validation and consistency checks
    - Implement conflict resolution with priority-based mechanisms
    - _Requirements: 4.3, 4.5_

  - [ ] 9.4 Write property test for data consistency
    - **Property 10: Database Consistency Maintenance**
    - **Validates: Requirements 4.3**

- [ ] 10. Implement advanced error handling and resilience
  - [ ] 10.1 Create intelligent retry mechanisms for all external APIs
    - Implement exponential backoff with jitter for API failures
    - Set up circuit breaker patterns for service degradation
    - Create fallback mechanisms with cached data when services unavailable
    - _Requirements: 8.5, 7.5_

  - [ ] 10.2 Write property test for API retry mechanisms
    - **Property 20: Intelligent API Retry Mechanisms**
    - **Validates: Requirements 8.5**

  - [ ] 10.3 Implement priority-based rate limiting and queuing
    - Create intelligent rate limiting based on operation criticality
    - Set up priority queues for urgent vs. routine operations
    - Implement adaptive rate limiting based on API response patterns
    - _Requirements: 7.6_

  - [ ] 10.4 Write property test for intelligent rate limiting
    - **Property 15: Intelligent Rate Limiting and Priority Queuing**
    - **Validates: Requirements 7.6**

- [ ] 11. Create Streamlit dashboard with geographic intelligence UI
  - [ ] 11.1 Implement real-time dashboard with WebSocket updates
    - Create module status monitoring with real-time updates
    - Implement geographic visualization for event impact and demand predictions
    - Set up interactive controls for manual intervention and overrides
    - _Requirements: 6.1, 6.5_

  - [ ] 11.2 Create specialized views for each module
    - Implement negotiation tracking view with supplier conversation status
    - Create hyper-local forecasting view with geographic heat maps
    - Set up profit recovery dashboard with marketplace performance tracking
    - _Requirements: 6.2, 6.3, 6.4_

  - [ ] 11.3 Write unit tests for dashboard functionality
    - Test real-time updates, geographic visualizations, and user interactions
    - Mock WebSocket connections and external data sources
    - _Requirements: 6.1, 6.5_

- [ ] 12. Implement comprehensive testing and validation
  - [ ] 12.1 Create property-based test suite with Hypothesis
    - Set up geographic coordinate generation and boundary testing
    - Implement marketplace data generation for profit optimization testing
    - Create multi-language communication testing for cultural adaptation
    - _Requirements: All correctness properties_

  - [ ] 12.2 Implement integration testing with external API sandboxes
    - Set up testing with PredictHQ, Tavily, and marketplace API sandboxes
    - Create end-to-end testing scenarios for complete workflows
    - Implement performance testing for real-time web intelligence queries
    - _Requirements: 8.1, 8.2, 3.4_

  - [ ] 12.3 Write comprehensive unit test coverage
    - Test all individual components with mocked dependencies
    - Validate error handling and edge cases for each module
    - Ensure proper cleanup and resource management
    - _Requirements: All requirements_

- [ ] 13. Final integration and optimization
  - [ ] 13.1 Optimize database queries and add performance monitoring
    - Create database indexes for frequently queried geographic and temporal data
    - Implement query optimization for real-time forecasting and profit calculations
    - Set up performance monitoring and alerting for system bottlenecks
    - _Requirements: 5.1, 12.1_

  - [ ] 13.2 Implement production deployment configuration
    - Create Docker containers for all services with proper orchestration
    - Set up environment-specific configuration for development, staging, production
    - Implement health checks and monitoring for all external API integrations
    - _Requirements: 7.5, 8.5_

  - [ ] 13.3 Create comprehensive documentation and API specifications
    - Generate OpenAPI documentation for all FastAPI endpoints
    - Create deployment guides and configuration documentation
    - Document all external API integrations and rate limiting strategies
    - _Requirements: 6.6_

- [ ] 14. Final checkpoint - Complete system validation
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- All tasks are required for a comprehensive, production-ready system
- Each task references specific requirements for traceability and validation
- Checkpoints ensure incremental validation and allow for user feedback
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples, edge cases, and integration points
- The implementation builds incrementally from infrastructure through individual modules to full integration
- External API integrations include proper error handling, rate limiting, and fallback mechanisms
- Geographic intelligence capabilities are integrated throughout for hyper-local optimization
- Profit recovery optimization is built into the Salvager module with marketplace automation
- Real-time web intelligence using Tavily API enhances all modules with current market data