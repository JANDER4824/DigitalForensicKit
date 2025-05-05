# API Reference - DigitalForensicKit

## core.evidence.Evidence

```python
Evidence(path, evidence_type, description="", case_id=None)
```
- Modela evidencia digital, calcula hashes y mantiene cadena de custodia.

## core.report.ReportGenerator

```python
ReportGenerator(case_name, author, output_dir="reports")
```
- `add_section(title, content)`
- `generate_pdf(filename, evidence_hashes=None)`
- `generate_html(filename)`
- `generate_json(filename)`
- `export_IOCs(ioc_list, fmt="stix"|"openioc", filename="iocs.xml")`

## modules.memory_analyzer.MemoryDumpAnalyzer

```python
MemoryDumpAnalyzer(dump_path, profile, case_id=None)
```
- `analyze_processes()`
- `analyze_hidden_processes()`
- `extract_iocs()`
- `extract_network_connections()`
- `extract_malware_artifacts()`
- `generate_timeline()`
- `run_plugin(plugin_name, **kwargs)`

## modules.disk_inspector.DiskInspector

```python
DiskInspector(image_path, case_id=None)
```
- `list_files(path="/")`
- `recover_deleted_files()`
- `analyze_metadata(file_path)`
- `search_file_signatures(signature)`
- `analyze_mft()`
- `extract_browser_artifacts()`
- `analyze_logs()`

## modules.network_forensics.NetworkForensics

```python
NetworkForensics(pcap_path, case_id=None)
```
- `analyze_sessions()`
- `extract_files()`
- `detect_anomalies()`
- `identify_protocols()`
- `analyze_flows()`
- `visualize_connections()`
- `detect_malicious_domains()`

## modules.log_parser.LogParser

```python
LogParser(log_paths, case_id=None)
```
- `parse_logs()`
- `correlate_events()`
- `detect_anomalies()`
- `filter_events(keyword)`
- `visualize_timeline()`