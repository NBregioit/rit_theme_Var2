import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def customerGroups():
    groups = toolkit.get_action('group_list')(data_dict={'all_fields': True})
    return groups

def newDatasets():
    packagelist = toolkit.get_action('current_package_list_with_resources')({},{'limit': 6})
    return packagelist

class RitThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'rit_theme')

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'customer_groups': customerGroups,'newest_Data': newDatasets}
