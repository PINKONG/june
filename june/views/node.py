# coding: utf-8

from flask import Blueprint
from flask import render_template, redirect, url_for
from ..models import Node
from ..forms import NodeForm
from ..helpers import require_staff


__all__ = ['bp']

bp = Blueprint('node', __name__)


@bp.route('/create', methods=['GET', 'POST'])
@require_staff
def create():
    """
    Create a node by staff members.
    """
    form = NodeForm()
    if form.validate_on_submit():
        node = form.save()
        return redirect(url_for('.view', urlname=node.urlname))
    return render_template('node/create.html', form=form)


@bp.route('/<urlname>')
def view(urlname):
    """
    The view page of the Node.

    The node page should contain the information of the node, and topics
    in this node.

    :param urlname: the urlname of the Node model
    """

    node = Node.query.filter_by(urlname=urlname).first_or_404()
    # TODO
    return render_template('node/view.html', node=node)


@bp.route('/<urlname>/edit')
@require_staff
def edit(urlname):
    """
    Edit a node by staff members.

    :param urlname: the urlname of the Node model
    """
    pass
