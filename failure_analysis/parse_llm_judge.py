import re
import logging

def parse_responses(responses):
    """
    Parse the LLM responses to extract yes/no answers for each failure mode.
    
    Args:
        responses: List of LLM responses evaluating traces
        
    Returns:
        Dictionary mapping failure mode codes to lists of binary values (0 for no, 1 for yes)
    """

    # Initialize dictionary with empty lists for each failure mode
    failure_modes = {
        f"FM{i + 1}": [] for i in range(4)
    }
    tot_response_cnt = 0
    for i, response in enumerate(responses):
        try:
            # Clean up the response - remove @@ markers if present
            cleaned_response = response.strip()
            if cleaned_response.startswith('@@'):
                cleaned_response = cleaned_response[2:]
            if cleaned_response.endswith('@@'):
                cleaned_response = cleaned_response[:-2]
            
            # Process each failure mode
            has_mode = False
            for mode in failure_modes.keys():
                # Various patterns to match different response formats
                patterns = [
                    # Format with C. prefix and colon
                    rf"B\..*?{mode}.*?(yes|no)",
                    # Format with just C prefix without dot
                    rf"B{mode}\s+(yes|no)",
                    # Format with mode directly (with or without spaces)
                    rf"{mode}\s*[:]\s*(yes|no)",
                    rf"{mode}\s+(yes|no)",
                    # Format with newlines
                    rf"{mode}\s*\n\s*(yes|no)",
                    # Format with C prefix and newlines
                    rf"B\.{mode}\s*\n\s*(yes|no)"
                ]
                
                found = False
                for pattern in patterns:
                    matches = re.findall(pattern, cleaned_response, re.IGNORECASE | re.DOTALL)
                    if matches:
                        # Use the first match
                        value = 1 if matches[0].lower() == 'yes' else 0
                        failure_modes[mode].append(value)
                        found = True
                        has_mode = True
                        break
                
                if not found:
                    # If we still can't find a match, try a more general approach
                    # Look for the mode number followed by any text and then yes/no
                    general_pattern = rf"(?:B\.)?{mode}.*?(yes|no)"
                    match = re.search(general_pattern, cleaned_response, re.IGNORECASE | re.DOTALL)
                    
                    if match:
                        value = 1 if match.group(1).lower() == 'yes' else 0
                        failure_modes[mode].append(value)
                        has_mode = True
                    else:
                        # If all attempts fail, default to 'no'
                        logging.warning(f"Warning: Could not find mode {mode} in response {i}")
                        failure_modes[mode].append(0)
            if has_mode == True:
                tot_response_cnt += 1
                    
        except Exception as e:
            print(f"Error processing response {i}: {e}")
            # If there's an error, default to 'no' for all modes for this response
            for mode in failure_modes:
                if len(failure_modes[mode]) <= i:  # Only append if we haven't already
                    failure_modes[mode].append(0)
    
    # Ensure all lists have the same length
    max_length = max(len(values) for values in failure_modes.values())
    for mode in failure_modes:
        if len(failure_modes[mode]) < max_length:
            failure_modes[mode].extend([0] * (max_length - len(failure_modes[mode])))
    
    return failure_modes, tot_response_cnt