import cwlgen

cwl_tool = cwlgen.CommandLineTool(tool_id='knime', label='execute a knime workflow', base_command='/usr/share/java/knime-desktop/knime');

cwl_tool.arguments = ['-reset', '-nosplash', '-application', 'org.knime.product.KNIME_BATCH_APPLICATION'];

file_binding = cwlgen.CommandLineBinding(prefix="-workflowFile=", separate=False);

input_file = cwlgen.CommandInputParameter('workflowFile', param_type='File', input_binding=file_binding, doc='workflow file');
cwl_tool.inputs.append(input_file)

# Slight output hack:
output = cwlgen.CommandOutputParameter('output', output_binding=cwlgen.CommandOutputBinding(output_eval=""), doc='output of workflow run', param_type="string")
cwl_tool.outputs.append(output)

cwl_tool.doc = "execute a knime workflow"
metadata = {'name': 'knime', 'about' : 'executre a knime workflow'}
cwl_tool.metadata = cwlgen.Metadata(**metadata)

cwl_tool.export();
cwl_tool.export(outfile="output/knime.cwl");
