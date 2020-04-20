# -*- coding: utf-8 -*-
from odoo import fields , models, api, _

class ChannelMappings(models.Model):
	_name="channel.mappings"
	_order = 'need_sync'

	@api.model
	def _needaction_domain_get(self):
		return [('need_sync', '=', 'yes')]

	@api.model
	def _channel_domain_get(self):
		return [('state', '=', 'validate')]

	@api.model
	def eComStoreUsed(self):
		channel_list = []
		channel_list = self.env['multi.channel.sale'].get_channel()
		return channel_list

	name = fields.Char(
		compute='_compute_name'
	)
	channel_id = fields.Many2one(
		comodel_name='multi.channel.sale',
		string='Instance',
		required=True,
		domain=_channel_domain_get
	)
	ecom_store = fields.Selection(
		selection='eComStoreUsed',
		string="Channel",
	)
	store_id =  fields.Char(
		string='Store ID',
	)
	need_sync = fields.Selection(
		selection=(('yes','Yes'),('no','No')),
		string='Update Required',
		default='no',
		required=True
	)
		
	operation = fields.Selection(
		selection=[('import','Import'),
		('export','Export')],
		string="Operation",
		default="import",
		required=True
		)
		
 	# _sql_constraints = [
  #       ('channel_store_store_id_uniq',
  #       	'unique(channel_id, store_id)',
  #       	'Store Object ID must be unique for channel mapping!'),
  #   ]
	def _compute_name(self):
		pass


	@api.model
	def get_need_sync_mapping(self,domain):
	    domain = domain and []
	    map_domain =domain+ [
	        ('need_sync', 'in', ['yes']),
	    ]
	    return self.search(map_domain)
